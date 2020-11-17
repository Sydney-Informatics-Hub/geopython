---
title: "Python for Geoscientists"
---

<div class="questions">  
### Questions
- What is Python?
- Why do you want to learn Python?
</div>

<div class="objectives">  
### Objectives
- Understand the Python ecosystem and other tools.
</div>



This course we will introduce you to foundations of Python programming. We will utilise common geosicence data types (geospatial, temporal, vector, raster, etc) to demonstrate a variety of practical workflows and showcase fundamental capabilities of Python. We will carry out exploratory, analytical, computational and machine learning analyses on these datasets. At the end of the course you will be able to adapt these workflows to your own datasets. 

The course is presented by the Sydney Informatics Hub on behalf of the Petroleum Exploration Society of Australia.


# What is Python?

The Python programming language was written in the 1980's. It is an interpreted and high-level language, this makes it easy to use for rapid development with lots of flexibility. Version 2.0 was released in 2000. Version 3.0 was released in 2008 (the current version is 3.9.0). 

I use it everyday to:

* Automate tasks (do things millions of times easily)
* Calculate big numbers (can solve most computational problems)
* Format and analyse data
* Process images

There are many comparable languages (e.g. R, Julia, C++, bash, Matlab, Java).
But there are a few reasons to favour Python:

* Python is free and open-source. 
* There is a large community of people using it all over the world on different projects, which means there is a lot of help and documentation.
* There are [millions](https://github.com/search?l=Python&q=python&type=Repositories) of codes, packages, libraries, and extensions. Some that leverage other programming languages to make your Python tasks fast, efficient and capable of doing whatever you need it to.

# How do we use Python? Terminals and Notebooks.

Traditionally one writes a "Python script file", like a recipe of instructions, and Python executes the script.

Simply, you can create python files in a text editor:
```
print("Hello World")
```

Save this as ```hello.py``` and execute it with ```python hello.py```.

As you go deeper into Python, you will see more advanced syntax:
```
#!/usr/bin/env python

'''
A Python program which greets the Earth!
Nathaniel Butterworth
PESA/SIH Python course

usage: python helloworld_advanced.py
'''

def main():
    print("Hello World! This is basically the same result, but a different way to get there.")

if __name__ == '__main__':
    main()
```

Once again, you can save this in a text editor as ```hello_advanced.py``` and execute with ```python hello_advanced.py```.

You can also start a Python IDE session, and execute commands one by one.

A handy tool is the Jupyter Notebook (modelled from Mathematica's Notebooks), that we will predominately be using throughout this course. They are good for the kind of non-development focused Python tasks you may need.

There are also online environments that can host Python code and notebooks for you.

Throughout the course you will see when and why to use different environments.

Now let's get into in the practical session!

<div class="keypoints">
### Key points
- Python is a programming language.
- There is a rich ecosystem of tools around creating and deploying Python code.
</div>
