/*                                              Program 1
 * Design and implement C/C++ Program to find Minimum Cost Spanning Tree of a given connected undirected
 * graph using Kruskal's algorithm
 */

#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

int a,b,c[20][20],i,j,k,min,n,parent[10],u,v;
int mincost=0,ne=0;

void kruskals(){
	for(i=1;i<=n;i++)
		parent[i]=0;
	while(ne!=n-1){
		min=INT_MAX;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				if(c[i][j]<min){
					min=c[i][j];
					u=a=i;
					v=b=j;
				}
		while(parent[u]!=0)
			u=parent[u];
		while(parent[v]!=0)
		v=parent[v];
		if(u!=v){
			printf("%d ----> %d = %d\n",a,b,min);
			parent[v]=u;
			ne+=1;
			mincost+=min;
		}
		c[a][b]=c[b][a]=INT_MAX;
	}
	printf("\nMincost = %d\n",mincost);
}

void help(char argv[]){
	printf(\
		"Usage : %s v [size] m [num1] [num2] ... [numN] \
		\n Options : \
		\n \t v Size of the array \
		\n \t m Elements of the array \
		\n \t h Display this help message and exit\n",argv \
	);
}

int main(int argc,char *argv[]){
	if(argc==1){
		help(argv[0]);
		exit(EXIT_SUCCESS);
	}
	for(i=1;i<argc;i++)
		switch(*argv[i]){
			case 'v':
				n=atoi(argv[++i]);
				break;
			case 'm':
				for(j=1;j<=n;j++)
					for(k=1;k<=n;k++)
						c[j][k]=atoi(argv[++i]);
				break;
			case 'h':
			default:
				help(argv[0]);
				exit(EXIT_SUCCESS);
		}
	kruskals();
	return EXIT_SUCCESS;
}
