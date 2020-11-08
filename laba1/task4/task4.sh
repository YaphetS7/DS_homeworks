mkdir abc
mkdir xyz

touch abc/file.txt

link abc/file.txt xyz/linked_file.txt

find . -inum "$(stat -c '%i' abc/file.txt)" >> ex4.txt

find . -inum "$(stat -c '%i' abc/file.txt)" -exec rm {} \;
