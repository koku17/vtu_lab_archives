#include<stdio.h>

float weight[20],profit[20],capacity,ratio[20],temp,x[20],tp=0;
int n,i,j,u;

void knapsack(int n,float weight[],float profit[],float capacity){
	u=capacity;
	for(i=0;i<n;i++)
		x[i]=0.0;
	for(i=0;i<n;i++)
		if(weight[i]>u)
			break;
		else{
			x[i]=1.0;
			tp+=profit[i];
			u-=weight[i];
		}
	if(i<n)
		x[i]=u/weight[i];
	tp+=x[i]*profit[i];

	printf("\nThe result vector is :\n");
	for(i=0;i<n;i++)
		printf("%f\n",x[i]);
	printf("\nMaximum profit is %f\n",tp);
}

void main(){
	printf("Enter the number of objects : ");
	scanf("%d",&n);

	printf("\nEnter the weights and profits of each object :\n");
	for(i=0;i<n;i++)
		scanf("%f%f",&weight[i],&profit[i]);

	printf("\nEnter the capacity of Knapsack : ");
	scanf("%f",&capacity);
	for(i=0;i<n;i++)
		ratio[i]=profit[i]/weight[i];

	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
			if(ratio[i]<ratio[j]){
				temp=ratio[j];
				ratio[j]=ratio[i];
				ratio[i]=temp;
				temp=weight[j];
				weight[j]=weight[i];
				weight[i]=temp;
				temp=profit[j];
				profit[j]=profit[i];
				profit[i]=temp;
			}
	knapsack(n,weight,profit,capacity);
}
