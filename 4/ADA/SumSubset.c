#include<stdio.h>
#define MAX 10

int i,n,s[MAX],sum=0,x[MAX],d;

void sumofsub(int p,int k,int r){
	x[k]=1;
	if((p+s[k])==d){
		for(i=0;i<=k;i++)
			if(x[i]==1)
				printf("%3d ",s[i]);
		printf("\n");
	}else if(p+s[k]+s[k+1]<=d)
		sumofsub(p+s[k],k+1,r-s[k]);
	if(p+r-s[k]>=d&&p+s[k+1]<=d){
		x[k]=0;
		sumofsub(p,k+1,r-s[k]);
	}
}

int main(){
	printf("Enter the n value : ");
	scanf("%d",&n);

	if(n>MAX){
		printf("\nn should be less than or equal to %d\n",MAX);
		return 1;
	}

	printf("\nEnter the set in increasing order : ");
	for(i=0;i<n;i++)
		scanf("%d",&s[i]);

	printf("\nEnter the max subset value : ");
	scanf("%d",&d);

	for(i=0;i<n;i++)
		sum+=s[i];

	if(sum<d||s[0]>d)
		printf("\nNo subset possible !\n");
	else
		sumofsub(0,0,sum);
	return 0;
}
