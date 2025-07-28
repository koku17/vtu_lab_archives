/*						Program 2
 * Design and implement C/C++ Program to find Minimum Cost Spanning Tree of a given connected undirected graph
 * using Prim's algorithm
 */

#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

int c[10][10],elec[10],i,j,k,min,n,u,v;
int ne=0,mincost=0;

void prims(){
	for(i=1;i<=n;i++)
		elec[i]=0;
	elec[1]=1;
	while(ne!=n-1){
		min=INT_MAX;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				if(elec[i]==1&&c[i][j]<min){
					min=c[i][j];
					u=i;
					v=j;
				}
		if(elec[v]!=1){
			printf("\n%d ----> %d = %d",u,v,min);
			elec[v]=u;
			ne+=1;
			mincost+=min;
		}
		c[u][v]=c[v][u]=INT_MAX;
	}
	printf("\n\nMincost = %d\n",mincost);
}

void help(char argv[]){
        printf(\
                "Usage : %s v [size] m [num1] [num2] ... [numN] \
                \n Options : \
                \n \t v Size of the array \
                \n \t m Insert the array \
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
	prims();
	return EXIT_SUCCESS;
}
