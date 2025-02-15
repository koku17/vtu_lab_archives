#include<stdio.h>
#include<stdlib.h>

int a[10][10],i,indegree[10],j,k=0,n,s[10],sum,t[10],top=-1,u,v;

void find_degree(){
	for(j=0;j<n;j++){
		sum=0;
		for(i=0;i<n;i++)
			sum+=a[i][j];
		indegree[j]=sum;
	}
}

void topo(){
	find_degree();
	for(i=0;i<n;i++)
		if(indegree[i]==0)
			s[++top]=i;
	while(top!=-1){
		u=s[top--];
		t[k++]=u;
		for(v=0;v<n;v++)
			if(a[u][v]==1){
				indegree[v]--;
				if(indegree[v]==0)
					s[++top]=v;
			}
	}
	printf("\nTopological Ordering :\n");
	for(i=0;i<n;i++)
		printf("%d ",t[i]);
	printf("\n");
}

void main(){
	printf("Enter the number of nodes : ");
	scanf("%d",&n);
	printf("\nEnter the adjacency matrix :\n");
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			scanf("%d",&a[i][j]);
	topo();
}
