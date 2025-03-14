#include<stdio.h>
#include<stdlib.h>

void warsh(int p[][10],int n){
	for(int k=1;k<=n;k++)
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				p[i][j]=p[i][j]||p[i][k]&&p[k][j];
}

int main(){
	int a[10][10],n;
	printf("\nEnter the n value : ");
	scanf("%d",&n);
	printf("\nEnter the graph data :\n");
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			scanf("%d",&a[i][j]);
	warsh(a,n);

	printf("\nResultant path matrix\n");
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++)
			printf("%d ",a[i][j]);
		printf("\n");
	}
	return 0;
}
