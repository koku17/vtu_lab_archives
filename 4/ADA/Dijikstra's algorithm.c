#include<stdio.h>
#define INF 999

int c[10][10],d[10],i,j,min,n,s,sum,u,v[10];

void dijkstra(int c[10][10],int n,int s,int d[10]){
	for(i=1;i<=n;i++){
		d[i]=c[s][i];
		v[i]=0;
	}

	v[s]=1;

	for(i=1;i<=n;i++){
		min=INF;
		for(j=1;j<=n;j++)
			if(v[j]==0&&d[j]<min){
				min=d[j];
				u=j;
			}
		v[u]=1;
		for(j=1;j<=n;j++)
			if(v[j]==0&&(d[u]+c[u][j])<d[j])
				d[j]=d[u]+c[u][j];
	}
}

int main(){
	printf("Enter n value : ");
	scanf("%d",&n);

	printf("\nEnter the graph data :\n");
	for(i=1;i<=n;i++)
		for(j=1;j<=n;j++)
			scanf("%d",&c[i][j]);

	printf("\nEnter the souce node : ");
	scanf("%d",&s);
	dijkstra(c,n,s,d);

	printf("\n");
	for(i=1;i<=n;i++)
		printf("Shortest distance from %d to %d is %d\n",s,i,d[i]);
	return 0;
}
