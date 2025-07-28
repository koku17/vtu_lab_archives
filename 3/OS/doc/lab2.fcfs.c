#include<stdio.h>
#include<stdlib.h>

int main(){
	int bt[20],wt[20],tat[20],i,n;
	float avwt,avtat;
	printf("Enter the number of process -- ");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		printf("Enter the burst time for the process %d -- ",i);
		scanf("%d",&bt[i]);
	}
	wt[0]=avwt=0;
	tat[0]=avtat=bt[0];

	for(i=1;i<n;i++){
		wt[i]=wt[i-1]+bt[i-1];
		tat[i]=tat[i-1]+bt[i];
		avwt+=wt[i];
		avtat+=tat[i];
	}

	printf("\nProcess\t Burst time\t Waiting Time\t Turnaround Time\n");
	for(i=0;i<n;i++)
		printf("p%d\t %d\t\t %d\t\t %d\n",i,bt[i],wt[i],tat[i]);
	printf("\nAverage waiting time -- %f",avwt/n);
	printf("\nAverage Turnaround time -- %f\n",avtat/n);
	exit(0);
}
