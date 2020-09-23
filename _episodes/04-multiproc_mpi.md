---
title: "4. Traditional python approaches to multi cpu and nodes"
teaching: 25
exercises: 5
questions:
- "How to utilise multiple cpus and nodes on Artemis"
objectives:
- "Discover python multiprocessing and mpi execution"
keypoints:
- "load multiprocessing library to execute a function in a parallel manner"

---

## Python Multiprocessing

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
