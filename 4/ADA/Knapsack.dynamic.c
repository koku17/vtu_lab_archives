#include<stdio.h>

int i,m,mp,n,p[20],w[20];

int max(int a,int b){
	return a>b?a:b;
}

int knapsack(int i,int m){
	if(i==n)
		return w[i]>m?0:p[i];
	if(w[i]>m)
		return knapsack(i+1,m);
	return max(knapsack(i+1,m),knapsack(i+1,m-w[i])+p[i]);
}

void main(){
	printf("Enter the number of objects : ");
	scanf("%d",&n);

	printf("\nEnter the weights and profits of each object :\n");
	for(i=1;i<=n;i++)
		scanf("%d%d",&w[i],&p[i]);

	printf("\nEnter the capacity of Knapsack : ");
	scanf("%d",&m);
	printf("\nThe maximum profit is %d\n",knapsack(1,m));
}
