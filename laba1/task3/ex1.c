#include <stdio.h>

int main(){

FILE *ptr;

ptr = fopen("newfile.txt", "w");

int pid = fork();

if(pid == 0){
	fprintf(ptr, "%d", 100);
}

return 0;
}