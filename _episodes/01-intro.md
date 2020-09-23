---
title: "1. Accelerating Python"
teaching: 10
exercises: 0
questions:
- "Who are the Sydney Informatics Hub?"
- "How do you make your Python faster?"
objectives:
- "Understand the Accelerated Python ecosystem."
keypoints:
- "SIH is availble to researchers to help them research!"
- "Many ways to make Python go faster."
---
This episode introduces the [Sydney Informatics Hub](https://informatics.sydney.edu.au/), and puts into context the desire to make our Python code/scripts run faster and efficiently.


# The Sydney Informatics Hub

The Sydney Informatics Hub (SIH) is a _[Core Research Facility](https://sydney.edu.au/research/facilities.html)_ of the University of Sydney. Core Research Facilities centralise essential research equipment and services that would otherwise be too expensive or impractical for individual Faculties to purchase and maintain. The classic example might be the room-size electron-microscopes, built into specialised rooms in the Sydney Microscopy & Microanalysis unit.

<figure>
  <img src="{{ page.root }}/fig/01_crf.png" style="margin:10px;width:600px"/>
  <figcaption> USyd Core Research Facilities <a href="https://sydney.edu.au/research/facilities.html">https://sydney.edu.au/research/facilities.html</a></figcaption>
</figure><br>

**Artemis HPC** itself is a multi-million dollar set of equipment, a 'supercomputer', and is the main piece of equipment supported by SIH. However, we also provide a wide range of research services to aid investigators, such as:

* [Training and workshops](https://sydney.edu.au/research/facilities/sydney-informatics-hub/workshops-and-training.html)
* [Project consulting and assisstance](https://sydney.edu.au/research/facilities/sydney-informatics-hub/project-support.html) with Statistics, Data Science, Research Engineering, Bioinformatics, Modeling/Simulation/Visualisation.
* [Research data management](https://sydney.edu.au/research/facilities/sydney-informatics-hub/digital-research-infrastructure.html) consulting and platform support.

We also aim to cultivate a **data community** at USyd, organising monthly [Hacky Hours](https://sydney.edu.au/research/facilities/sydney-informatics-hub/workshops-and-training/hacky-hour.html), outside training events (eg NVIDIA, Pawsey Center), and data/coding-related events. Look out for everthing happening on our [calander](https://www.sydney.edu.au/research/facilities/sydney-informatics-hub/workshops-and-training/training-calendar.html) or contact us (at sih.info@sydney.edu.au) to get some digital collaboration going.

<br>
# Acceleration, Paralleisation, Vectorising, Threading, make-Python-go-fast 

We will cover a few of the ways that you can potentially speed up Python. As we will learn there are multitudes of methods to make Python code more efficient, and also different implentations of libraries, tools, techniques that can all be utilised depending on how your code and/or data is organised. This is a rich and evolving ecosystem and there is no one perfect way to implement efficiencies.

Some key words that might come up:

* Vectorisation
* MPI message parsing interface
* CPU, core, node, thread, process, worker, job, task
* Parallelisation
* Python decorators and functional programming.


<br>
# Course pre-requisites
You should have some experience with Python. You should be able to connect to a remote computer (i.e. Artemis) via ssh and submit a job to a scheduler.


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

Let's get started with some examples....


