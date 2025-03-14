#include<stdio.h>
#include<stdlib.h>

int main(){
	int p[20],bt[20],wt[20],tat[20],i,k,n,temp;
	float wtavg,tatavg;
	printf("Enter the number of process : ");
	scanf("%d",&n);

	for(i=0;i<n;i++){
		p[i]=i;
		printf("Enter the burst time for the process %d : ",i);
		scanf("%d",&bt[i]);
	}

	for(i=0;i<n;i++)
		for(k=i+1;k<n;k++)
			if(bt[i]>bt[k]){
				temp=bt[i];
				bt[i]=bt[k];
				bt[k]=temp;
				temp=p[i];
				p[i]=p[k];
				p[k]=temp;
			}
	wt[0]=wtavg=0;
	tat[0]=tatavg=bt[0];

	for(i=1;i<n;i++){
		wt[i]=wt[i-1]+bt[i-1];
		tat[i]=tat[i-1]+bt[i];
		wtavg+=wt[i];
		tatavg+=tat[i];
	}

	printf("\nProcess\t Burst time\t Waiting Time\t Turnaround Time\n");
	for(i=0;i<n;i++)
		printf("p%d\t %d\t\t %d\t\t %d\n",p[i],bt[i],wt[i],tat[i]);
	printf("\nAverage waiting time : %f",wtavg/n);
	printf("\nAverage Turnaround time : %f\n",tatavg/n);
	return 0;
}
