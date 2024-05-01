#include<stdio.h>
#include<stdlib.h>

int c[10][10],elec[10],i,j,min,n,u,v;
int ne=0,mincost=0;

void prims(){
	for(i=1;i<=n;i++)
		elec[i]=0;
	elec[1]=1;
	while(ne!=n-1){
		min=9999;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				if(elec[i]==1&&c[i][j]<min){
					min=c[i][j];
					u=i;
					v=j;
				}
		if(elec[v]!=1){
			printf("\n%d ----> %d=%d",u,v,min);
			elec[v]=u;
			ne+=1;
			mincost+=min;
		}
		c[u][v]=c[v][u]=9999;
	}
	printf("\n\nMincost=%d\n",mincost);
}

int main(){
	printf("Enter the number of vertices : ");
	scanf("%d",&n);
	printf("Enter the cost matrix :\n");
	for(i=1;i<=n;i++)
		for(j=1;j<=n;j++)
			scanf("%d",&c[i][j]);
	prims();
	return 0;
}
