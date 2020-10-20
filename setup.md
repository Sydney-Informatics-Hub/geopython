---
title: Setup
layout: page
root: "."
---

# 1. Get a Python client
We generally use and recommend Miniconda Python distribution: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html). But feel free to use whatever one works for you.
However you can do all the exercises using remote resources for the training sessions. But it is probably best to have a local working Python environment.

<br>

## 2. Python environemnt
To run all the commands today in your own Python installation, you can set up an environemnt with something like this:

wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh

~~~
conda create -n dd dask==2.11.0 distributed==2.11.0 netCDF4==1.5.3 numpy==1.18.1 pandas==1.0.1 scipy==1.4.1 xarray==0.15.0 mpi4py==3.0.3 -c conda-forge
~~~

<br>

# 3. Get a shell terminal emulator

For some exercises you will need a **'terminal emulator'** program installed on your computer. Often just called a 'terminal', or 'shell terminal', 'shell client', terminal emulators give you a window with a _command line interface_ through which you can send commands to be executed by your computer.

## A. Linux systems

If you use Linux, then chances are you already know your shell and how to use it. Basically, just open your preferred terminal program and off you go! An X-Window server (X11) may also be useful if you want to be able to use GUIs; again, if you're using Linux you probably have one, and if you don't have one, it's probably because you intentionally disabled it!


## B. OSX (Mac computers and laptops)

Mac operating systems come with a terminal program, called Terminal. Just look for it in your Applications folder, or hit Command-Space and type 'terminal'.

<figure>
  <img src="{{ page.root }}/fig/s_terminal_app.png" width="500">
  <figcaption> <b>Terminal</b> is OSX's native terminal emulator.</figcaption>
</figure><br>

We also recommend installing [XQuartz](https://www.xquartz.org/), which will replace OSX's native X-Window server. XQuartz has some extra features that may offer better performance when using GUI programs. You'll need to log out and back in again after installing XQuartz in order for it to activate.

## C. Windows

If you're using a Windows machine, don't panic! You might not have used 'CMD' since Windows 95 but, rest assured, Windows still has a couple of terminal programs and shells buried in the Programs menu.

However, those aren't going to work for us, as you'll need extra programs and utilities to connect to Artemis, such as an _SSH_ implementation. To use connect to a remote machine on Windows, you have a several options, our recommeded ones are:

### i. MobaXterm (Simple Client)

MobaXterm, an SSH and telnet client, is another good simple option.

Head to [https://mobaxterm.mobatek.net/](https://mobaxterm.mobatek.net/download-home-edition.html) and download. You can install it to your computer, or just download the 'portable' edition and run it directly (without needing admin access to install anything). 

### ii. WSL and Ubuntu (Advanced Linux Emulation)

Install Ubuntu or some other Linux distro on the Windows Subsystem for Linux see [here for details](https://ubuntu.com/tutorials/tutorial-ubuntu-on-windows#1-overview). This one will give you a full suite of Linux functions and I like it for emulating Linux.

```
 sudo apt-get update
 sudo apt-get install build-essential
 sudo apt install libopenmpi-dev
 pip install dask==2.11.0 distributed==2.11.0 netCDF4==1.5.3 numpy==1.18.1 pandas==1.0.1 scipy==1.4.1 xarray==0.15.0 mpi4py==3.0.3 jupyter pyshp pandas swifter shapely
 ```

<br>


{% include links.md %}
