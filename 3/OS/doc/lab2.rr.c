#include<stdio.h>

int main(){
	int bu[10],wa[10],tat[10],ct[10],i,j,max,n,t;
	float awt,att,temp;
	awt=att=temp=0;

	printf("Enter the number of process : ");
	scanf("%d",&n);

	for(i=0;i<n;i++){
		printf("Enter the burst time for the process %d : ",i+1);
		scanf("%d",&bu[i]);
		ct[i]=bu[i];
	}

	printf("Enter the time slice : ");
	scanf("%d",&t);
	max=bu[0];

	for(i=1;i<n;i++)
		if(max<bu[i])
			max=bu[i];

	for(j=0;j<(max/t)+1;j++)
		for(i=0;i<n;i++)
			if(bu[i]!=0){
				if(bu[i]<=t){
					tat[i]=temp+bu[i];
					temp+=bu[i];
					bu[i]=0;
				}else{
					bu[i]-=t;
					temp+=t;
				}
			}

	for(i=0;i<n;i++){
		wa[i]=tat[i]-ct[i];
		att+=tat[i];
		awt+=wa[i];
	}

	printf("\nThe Average Turnaround time is : %f",att/n);
	printf("\nThe Average Waiting time is : %f",awt/n);
	printf("\nProcess\t Burst time\t Waiting Time\t Turnaround Time\n");
	for(i=0;i<n;i++)
		printf("%d\t %d\t\t %d\t\t %d\n",i+1,ct[i],wa[i],tat[i]);
	return 0;
}
