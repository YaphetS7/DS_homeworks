#include <stdio.h>

int main(){

FILE *ptr;

ptr = fopen("newfile.txt", "w");

int pid = fork();

if(pid == 0){ // child process
	fprintf(ptr, "%d", 100);
}
else{ // parent process 
	fprintf(ptr, "%d", 99);
}

return 0;
}