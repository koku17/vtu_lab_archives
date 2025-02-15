#include<stdio.h>
#include<stdlib.h>
#define INF 999

int min(int a,int b){
	return a<b?a:b;
}

void floyd(int p[][10],int n){
	for(int k=1;k<=n;k++)
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				p[i][j]=min(p[i][j],p[i][k]+p[k][j]);
}

int main(){
	int p[10][10],n;
	printf("Enter the n value : ");
	scanf("%d",&n);
	printf("\nEnter the graph data :\n");

	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			scanf("%d",&p[i][j]);
	floyd(p,n);
	printf("\nShortest path matrix :\n");
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++)
			if (p[i][j]==INF)
				printf("%4s","INF");
			else
				printf("%4d",p[i][j]);
		printf("\n");
	}
	return 0;
}
