---

### ex1.c vs ex5.c:

* gcc ex1.c -o out (or gcc ex5.c -o out)
* ./out
* cat newfile.txt

#### Output: 99100 or 10099. So process after completion calls close() for all descriptors.


### ex2.c:

* gcc ex2.c -o out
* ./out
* cat newfile.txt

#### Output: 99, coz child process has not finished.


### ex3.c:

* gcc ex3.c -o out
* ./out &
* cat newfile.txt

#### Output: 100, coz parent process has not finished.


### ex4.c:

* gcc ex4.c -o out
* ./out &
* cat newfile.txt

#### Output: blank file, coz child and parent processes have not finished.


### Conclusion:

"The child inherits copies of the parent's set of open file descriptors.  
Each file descriptor in the child refers to the same open file description (see open(2)) as the corresponding file descriptor in the parent.  
This means that the two file descriptors share open file status flags, file offset, 
and signal-driven I/O attributes (see the description of F_SETOWN and F_SETSIG in fcntl(2))." [1]

## References: 
[1] - https://man7.org/linux/man-pages/man2/fork.2.html
