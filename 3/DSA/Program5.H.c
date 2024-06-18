#include<stdio.h>
#include<math.h>

void tower(int n,char beg,char aux,char end){
	if(n==0)
		printf("Illegal, Try with non-zero Positive Integers !\n");
	else if(n==1)
		printf("Move Disc from %c to %c\n",beg,end);
	else{
		tower(n-1,beg,end,aux);
		tower(1,beg,aux,end);
		tower(n-1,aux,beg,end);
	}
}

void main(){
	int n;
	printf("Enter the number of Discs :\n> ");
	scanf("%d",&n);
	printf("Tower of Hanoi for %d Disc has the following steps :\n",n);
	tower(n,'a','b','c');
	printf("\n\nTotal Number of moves are : %d\n",(int)pow(2,n)-1);
}
