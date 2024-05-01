#include<stdio.h>
#include<stdlib.h>

int a,b,c[10][10],i,j,min,n,parent[10],u,v;
int mincost=0,ne=0;

void kruskals(){
	for(i=1;i<=n;i++)
		parent[i]=0;
	while(ne!=n-1){
		min=9999;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				if(c[i][j]<min){
					min=c[i][j];
					u=a=i;
					v=b=j;
				}
		while(parent[u]!=0||parent[v]!=0)
			if(parent[u]!=0)
				u=parent[u];
			else
				v=parent[v];
		if(u!=v){
			printf("\n%d ----> %d=%d",a,b,min);
			parent[v]=u;
			ne+=1;
			mincost+=min;
		}
		c[a][b]=c[b][a]=9999;
	}
	printf("\n\nMincost=%d\n",mincost);
}

int main(){
	printf("Enter the number of vertices : ");
	scanf("%d",&n);
	printf("\nEnter the cost matrix :\n");
	for(i=1;i<=n;i++)
		for(j=1;j<=n;j++)
			scanf("%d",&c[i][j]);
	kruskals();
	return 0;
}
