---
title: "3. Connecting to Artemis HPC"
teaching: 5
exercises: 5
questions:
- "How can you scale up beyond your local machine?"
objectives:
- "Refresh how to connect to Artemis HPC"
keypoints:
- "Several methods and tools to connect to a remote machine"
- "Get access to more resources than your local computer"

---

# Connect to Artemis

If you followed the [Setup]({{ page.root }}/setup) instructions, then you should already have the required software installed. If not, _please go do this now_!

<h2 data-toc-text="via SSH command line"> Connect via SSH in a terminal (recommended)</h2>

Fire up your **terminal emulator** and connect to Artemis HPC via **SSH**. When you use Artemis for your research, these will be your **Unikey** and **Unikey password**; however, for this training course we'll be using _training accounts_, which are:

* Username: **ict_hpctrain\<N\>**, with N from 1-20 (replace _**\<N\>**_ with your assigned number)
* Password: _will be written on the whiteboard!_

~~~
ssh -X ict_hpctrain<N>@hpc.sydney.edu.au
~~~
{: .bash}

or, if using XQuartz on a Mac

~~~
ssh -Y ict_hpctrain<N>@hpc.sydney.edu.au
~~~
{: .bash}

The ```-X``` or ```-Y``` flags tell **ssh** to enable X-forwarding, which lets GUI programs on Artemis serve you graphical windows back on your local machine.


<figure>
  <img src="{{ page.root }}/fig/01_bash.png" style="margin:10px;width:600px"/>
  <figcaption> An iTerm2 terminal window on Mac</figcaption>
</figure><br>


If connecting for the first time on this machine, you may get the following output, requesting authorisation to connect to a new **host** server:

~~~
The authenticity of host 'hpc.sydney.edu.au (10.250.96.203)' can't be established.
RSA key fingerprint is SHA256:qq9FPWBcyvvOWOMdFs8uZES0tF3SVzJsNx1cdn56GSE.
Are you sure you want to continue connecting (yes/no)?
~~~
{: .output}

Enter 'yes'. You will then be asked for your password: type it and press 'enter', and you should then be logged in!

<figure>
  <img src="{{ page.root }}/fig/01_granted.png" style="margin:10px;width:630px"/>
  <figcaption> Access granted! </figcaption>
</figure><br>


<h2 data-toc-text="via SSH GUI apps"> Connecting via an SSH GUI (common for Windows users) </h2>

If you're on Windows, and followed the [Setup]({{ page.root }}/setup) guide, then you will likely be connecting through an X-window or shell client program, like 'X-Win32' or 'PuTTY'. Following the instructions in the [Setup]({{ page.root }}/setup) guide:
* Open your installed program
* Select the "Artemis" session you configured earlier
* Click 'Launch' (X-Win32) or 'Open' (PuTTY)

If this is the first time connecting to Artemis, you will be asked to authorise it as a trusted **host** server; click 'Accept' (X-Win32) or 'Yes' (PuTTY).

<figure>
  <img src="{{ page.root }}/fig/01_xwinhosts.png" style="margin:10px;height:240px"/>
  <img src="{{ page.root }}/fig/01_puttyhosts.png" style="margin:10px;height:250px"/>
  <figcaption> Unknown host challenges: X-Win32 (top), PuTTY (bottom) </figcaption>
</figure><br>

* If using 'X-Win32', enter your **password** and once entered, a terminal window connected to Artemis should open.

* If using 'PuTTY', enter your **username**, and then your **password** in the terminal window that appears. You should now be logged in to Artemis.

<figure>
  <img src="{{ page.root }}/fig/01_xwin.png" style="margin:10px;height:220px"/>
  <img src="{{ page.root }}/fig/01_putty.png" style="margin:10px;height:350px"/>
  <figcaption> Access granted! X-Win32 (top) cuts the welcome messages, PuTTY (bottom) </figcaption>
</figure><br>

<br>
