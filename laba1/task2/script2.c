#include <stdio.h>

int main(){
	
char str[100];

while(1){

	fgets(str, sizeof(str), stdin);

	system(str);

}

return 0;
}