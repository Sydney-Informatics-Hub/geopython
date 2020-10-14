---
title: "04a. Efficient Python methods"
teaching: 10
exercises: 15
questions:
- "Which method for acceleration should I choose?"
- "How do I utilise traditional python approaches to multi cpu and nodes"
objectives:
- "Learn simples methods to profile your code"
- "See how numpy and pandas use Vectorising to improve perfomance for some data"
- "Use MPI to communicate between workers"
- "Discover python multiprocessing and mpi execution"
keypoints:
- "Understand there are different ways to accelerate"
- "The best method depends on your algorithms, code and data"
- "load multiprocessing library to execute a function in a parallel manner"
---

This episode shows you a few of the basic tools that we can use in Python to make our code go faster. There is no perfect method for optimising code. Efficiency gains depend on what your end goal is, what libraries are available, what method or approach you want to take when writing algorithms, what your data is like, what hardware you have. Hopefully these notes will allow you to think about your problems from different perspectives to give you the best opportunity to make your development and execution as efficient as possible.

# Acceleration, Paralleisation, Vectorising, Threading, make-Python-go-fast 

We will cover a few of the ways that you can potentially speed up Python. As we will learn there are multitudes of methods to make Python code more efficient, and also different implentations of libraries, tools, techniques that can all be utilised depending on how your code and/or data is organised. This is a rich and evolving ecosystem and there is no one perfect way to implement efficiencies.

Some key words that might come up:

* Vectorisation
* MPI message parsing interface
* CPU, core, node, thread, process, worker, job, task
* Parallelisation
* Python decorators and functional programming.

<br>
# What does *parallel* mean?
Seperate workers or processes acting in an independent or semi-dependent manner. Independent processes ship data, program files and libraries to an isloated ecosystem where computation is performed Communication between workers can be achieved. Contrastingly there are also shared memory set ups where multiple computational resources are pooled together to work on the same data. 

Generally speaking parallel workflows fit different categories, which can make you think about how to write your code and what approaches to take.

### Embarrassingly parallel:
Requires no communication between processors. Utilise shared memory spaces.

* running same algorithm for a range of input parameters
* rendering video frames in computer animation
* Open MP implementations.

### Coarse/Fine-grained parallel:
Requires occasional or frequent communication between processors

* Uses a small number of processes on large data. 
* Fine grain uses a large number of small processes with very little communication. Improves computationally bound problems.
* MPI implementations.
* Some examples are finite difference time-stepping on parallel grid, finite element methods.

Traditional implemententations of paralellism  are done on a low level. However, open source software has ***evolved*** dramatically over the last few years allowing more ***high level implementations and concise 'pythonic' syntax*** that wraps around low level tools. The focus on this course is to use these modern high level implementations for use on Artemis.


# Profiling your code

Before you get stuck into making things fast, it is important to find out what is exactly slow in your code. Is it a particular function running slow? Or are you calling a really fast function a million times? You can save yourself a lot development time by profiling your code to give you an idea for where efficiencies can be found. Let's profile a simple Python script and then think about how we could make it faster.

Put this code in a script (or download from [here](https://sydney-informatics-hub.github.io/training.artemis.python/files/faster.py)):
~~~
#A test function to see how you can profile code for speedups

import time

def waithere():
	print("waiting for 1 second")
	time.sleep(1)

def add2(a=0,b=0):
	print("adding", a, "and", b)
	return(a+b)

def main():
	print("Hello, try timing some parts of this code!")
	waithere()	
	add2(4,7)
	add2(3,1)


if __name__=='__main__':
	main()
~~~
{: .python}

There are several ways to debug and profile Python, a very elegant and built in one is [cProfile](https://docs.python.org/3/library/profile.html)
It analyses your code as it executes. Run it with ```python -m cProfile faster.py```  and see the output of the script and the profiling:

~~~
Hello, try timing some parts of this code!
waiting for 1 second
adding 4 and 7
adding 3 and 1

12 function calls in 1.008 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    1.008    1.008 faster.py:12(main)
1    0.000    0.000    1.008    1.008 faster.py:2(<module>)
1    0.000    0.000    1.002    1.002 faster.py:4(waithere)
2    0.000    0.000    0.005    0.003 faster.py:8(add2)
1    0.000    0.000    1.008    1.008 {built-in method builtins.exec}
4    0.007    0.002    0.007    0.002 {built-in method builtins.print}
1    1.001    1.001    1.001    1.001 {built-in method time.sleep}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
~~~
{: .output}

You can now interrogate your code and see where you should devote your time to improving it.

Special note on style: Developing python software in a ***modular*** manner assists with debugging and time profiling.


# Loops and vectorising code with numpy and pandas

Your problem might be solved by using the fast way certain packages handle certain datatypes. 

Generally speaking, pandas and numpy libraries should be libraries you frequently use. They offer advantages in high performance computing including:
1. Efficient datastructures that under the hood are implemented in fast C code rather than python.
2. Promoting explicit use of datatype declarations - making memory management of data and functions working on this data, faster.
3. Elegant Syntax promoting consise behaviour. 
4. Data structures come with common built in functions that are designed to be used in a vectorised way.

Lets explore this last point on vectorisation with an example. Take this nested for loop [example](https://sydney-informatics-hub.github.io/training.artemis.python/files/vector.py):

~~~
#import packages
import numpy as np
import pandas as pd
import time 

#Create some data to work with
AllPubs = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=['user','publication','id','other'])
Users = pd.DataFrame(np.random.randint(0,100,size=(50, 1)), columns=['id'])

#This could perhaps be the id of a person and the list of publications they have made. 
#You want to match up their publications with some other list, 
#perhaps the publications they made by using Artemis.

#Create an emtpy dataframe to fill with the resulting matches
totalSlow=pd.DataFrame(columns=AllPubs.columns)
totalFast=pd.DataFrame(columns=AllPubs.columns)

~~~
{: .python}

Now compare the nested for-loop method:
~~~
tic=time.time()
for index,pub in AllPubs.iterrows():
  for index2,user in Users.iterrows():
    if user['id']==pub['id']:
      totalSlow=totalSlow.append(pub,ignore_index=True)
      
totalSlow=totalSlow.drop_duplicates()
toc=time.time()
print("Runtime:",toc-tic, "seconds")

~~~
{: .python}

Or the vectorised method:
~~~
tic=time.time()
totalFast=AllPubs[AllPubs['id'].isin(Users.id.tolist())]
totalFast=totalFast.drop_duplicates()
toc=time.time()
print("Runtime:",toc-tic, "seconds")

~~~
{: .python}


Which one is faster? Note the use of some really basic timing functions, these can help you understand the speed of your code.




# MPI: Message Passing Interface
MPI is a standardized and portable message-passing system designed to function on a wide variety of parallel computers.
The standard defines the syntax and semantics of a core of library routines useful to a wide range of users writing portable message-passing programs in C, C++, and Fortran. There are several well-tested and efficient implementations of MPI, many of which are open-source or in the public domain.

MPI for Python, found in [mpi4py](https://mpi4py.readthedocs.io/en/stable/index.html), provides bindings of the MPI standard for the Python programming language, allowing any Python program to exploit multiple processors. [This simple code](https://sydney-informatics-hub.github.io/training.artemis.python/files/mpi.py) demonstrates the collection of resources and how code is run on different processes:

~~~
#Run with:
#mpiexec -np 4 python mpi.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print("I am rank %d in group of %d processes." % (rank, size))
~~~
{: .python}

If you want to submit this python script on a High Performance Computing environment, the PBS script is below. Notice here we are requesting 4 seperate nodes in the PBS script. This amount aligns with the ```-np 4``` flag (number of processes), so each process is seperate and executed on different nodes on Artemis.
~~~
#!/bin/bash

#PBS -P Training
#PBS -N testmpi
#PBS -l select=4:ncpus=1:mem=1GB
#PBS -l walltime=00:10:00
#PBS -q defaultQ

cd $PBS_O_WORKDIR
module load python
module load openmpi-gcc

mpiexec -np 4 python mpi.py > mpi.out
~~~
{:. bash}

Let's now get stuck into some more specific use-cases and tools to use.



# Python Multiprocessing

The PBS resource request ```#PBS -l select=1:ncpus=1``` signals to the scheduler how many nodes and cpus you want your job to run with. But from within Python you may need more flexible ways to manage resources. This is traditionally done with the ***multiprocessing*** library. 

With multiprocessing, Python creates new processes. A process here can be thought of as almost a completely different program, though technically they are usually defined as a collection of resources where the resources include memory, file handles and things like that. 

One way to think about it is that each ***process runs in its own Python interpreter***, and multiprocessing farms out parts of your program to run on each process.

## Some terminology - Processes, threads and shared memory
A ***process*** is a collection of resources including program files and memory, that operates as an independent entity. Since each process has a seperate memory space, it can operate independently from other processes. It cannot easily access shared data in other processes.

A ***thread*** is the unit of execution within a process. A process can have anywhere from just one thread to many threads. Threads are considered lightweight because they use far less resources than processes. Threads also share the same memory space so are not independent.

<figure>
  <img src="{{ page.root }}/fig/process_v_thread.png" style="margin:6px;width:300px"/>
</figure><br>

<figure>
  <img src="{{ page.root }}/fig/process_threads_comparison.png" style="margin:6px;width:400px"/>
</figure><br>

Back to python, the multiprocessing library was designed to break down the **Global Interpreter Lock (GIL)** that limits one thread to control the Python interpreter. 

In Python, the things that are occurring simultaneously are called by different names (thread, task, process). While they all fall under the definition of concurrency (multiple things happening anaologous to different trains of thought), only multiprocessing actually runs these trains of thought at literally the same time. We will only cover multiprocessing here which assists in CPU bound operations - but keep in mind other methods exist (threading), whose implementation tends to be more low level. 

## Small demonstration of python multiprocessing library

Some basic concepts in the multiprocessing library are:
1. the ```Pool(processes)``` object creates a pool of processes. ```processes``` is the number of worker processes to use (i.e Python interpreters). If ```processes``` is ```None``` then the number returned by ```os.cpu_count()``` is used.
2. The ```map(function,list)``` attribute of this object uses the pool to map a defined function to a list/iterator object

To implement multiprocessing in its basic form.
Create a small python file called ```basic.py``` with the below code.
~~~
from multiprocessing import Pool

def addit(x):
        return x + 1

def main():
        print(addit(4))
        with Pool(2) as p:
                print(p.map(addit,[1,2,3]))

main()
~~~
{: .python}

Now, you run this in an interactive session.

~~~
qsub -I -P Training -l select=1:ncpus=2:mem=6GB -l walltime=00:10:00
~~~

Keep in mind the automatic behaviour for Artemis, once an interactive session has started, is to put you in your home directory. 

Now load in a Python 3 module we can use. Note, this is pre-installed on Artemis, you can use your own specific versions as required.
~~~
module load python/3.7.2
~~~

And run it with:
~~~
python basic.py
~~~

The output should be:
~~~
5
[2, 3, 4]
~~~
{: .output}

## Getting Data and Files for this Course:

Let's run a larger piece of code in the traditional PBS script manner that utilises the multiprocessing library. You will need some files for this and other training demonstrations covered today. 

If your not still in an interactive session, create another one. This is option but will make transfers faster - if there are enough cpu resources on the training node.

~~~
qsub -I -P Training -l select=1:ncpus=6:mem=6GB -l walltime=00:10:00
~~~

Lets create a working folder and copy data to it. This holds both data and files we'll use for the rest of this training session.

~~~
mkdir /project/Training/myname 
cd /project/Training/myname 
rsync -av /project/Training/AdvPyTrain/files/* ./files
rsync -av /project/Training/AdvPyTrain/data/* ./data
~~~

Please exit the interactive session once files and data has been loaded into your directory
~~~
exit
~~~

## Calculation of pi - submitting two scripts to compare multiprocessing advantage

<figure>
  <img src="{{ page.root }}/fig/calc_pi.png" style="margin:5px;width:400px"/>
</figure><br>

Navigate to the computepi_multiprocs.py file located in the files directory. Notice how the Pool object and map function sets off simulating an estimate of pi given a sequence of trails - the larger the trail number the closer the estimate is to pi. 

Run two scripts by sumitting the run_pi.pbs file to the scheduler. This pbs script should submit two jobs that approximate pi in the same way, except one using the multiprocessing library and is slightly faster even though the same Artemis resources are requested.

~~~
cd files
qsub run_pi.pbs
~~~

While it is running, have a look at the code.

When it is completed, check out the output of the two methods in ```out_pi.o?????```. Which method was faster? Did you get the kind of speed-up you were expecting?

## Keep in Mind

There is generally a sweet spot in how many processes you create to optimise the run time. A large number of python processes is generally not advisable, as it involves a large fixed cost in setting up many python interpreters and its supporting infrastructure. Play around with different numbers of processes in the pool(processes) statement to see how the runtime varies. 

## Useful links

[https://realpython.com/python-concurrency/](https://realpython.com/python-concurrency/)

[https://docs.python.org/3/library/multiprocessing.html](https://docs.python.org/3/library/multiprocessing.html)

[https://www.backblaze.com/blog/whats-the-diff-programs-processes-and-threads/](https://www.backblaze.com/blog/whats-the-diff-programs-processes-and-threads/)

[https://pawseysc.github.io/training.html](https://pawseysc.github.io/training.html)

<br>

___
**Notes**   
<sup id="f1">1[↩](#a1)</sup>As you should recall from the [Introduction to Artemis HPC]({{ site.sih_pages }}/training.artemis.introhpc/) course, the **scheduler** is the software that runs the cluster, allocating jobs to physical compute resources. Artemis HPC provides us with a separate 'mini-cluster' for _Training_, which has a separate PBS scheduler instance and dedicated resources.

___
<br>


