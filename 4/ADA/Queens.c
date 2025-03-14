#include<stdio.h>
#include<stdlib.h>
#define MAX 50

int c[MAX],count=1,i,j,n,r;
char cb[10][10];

int can_place(int c[],int r){
	for(i=0;i<r;i++)
		if(c[i]==c[r]||abs(c[i]-c[r])==abs(i-r))
			return 0;
	return 1;
}

void display(int c[],int n){
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			cb[i][j]='-';
	for(i=0;i<n;i++)
		cb[i][c[i]]='Q';
	for(i=0;i<n;i++){
		for(j=0;j<n;j++)
			printf("%2c",cb[i][j]);
		printf("\n");
	}
}

void n_queens(int n){
	r=0;
	c[r]=-1;
	while(r>=0){
		c[r]++;
		while(c[r]<n&&!can_place(c,r))
			c[r]++;
		if(c[r]<n){
			if(r==n-1){
				printf("Count : %d\n\n",count++);
				display(c,n);
				printf("\n");
			}else
				c[++r]=-1;
		}else
			r--;
	}
}

void main(){
	printf("Enter the no. of queens : ");
	scanf("%d",&n);
	n_queens(n);
}
