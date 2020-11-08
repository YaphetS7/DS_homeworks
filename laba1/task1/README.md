---

### For the start - execute command:
* sh shell_script.sh

### Output:

* execute pstree command:

After 1st fork() call (2 processes):

<img src="images/1.jpg" height=650 width=600>

After 2nd fork() call (4 processes):

<img src="images/2.jpg" height=650 width=600>

After 3nd fork() call (8 processes):

<img src="images/3.jpg" height=650 width=600>

After n fork() calls we have 2^n processes, coz each process calling next fork(). First process is out script.

