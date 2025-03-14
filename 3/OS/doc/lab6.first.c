#include <stdio.h>
#include <stdlib.h>
#define max 25

void main(){
	int frag[max],b[max],f[max],i,j,nb,nf,temp;
	static int bf[max],ff[max];

	printf("\nMemory Management Scheme-First Fit");
	printf("\nEnter the number of blocks : ");
	scanf("%d",&nb);

	printf("\nEnter the number of files : ");
	scanf("%d",&nf);

	printf("\nEnter the size of the blocks : \n");
	for(i=1;i<=nb;i++){
		printf("Block %d : ",i);
		scanf("%d",&b[i]);
	}

	printf("\nEnter the size of the files  : \n");
	for(i=1;i<=nf;i++){
		printf("File %d : ",i);
		scanf("%d",&f[i]);
	}

	for(i=1;i<=nf;i++){
		for(j=1;j<=nb;j++)
			if(bf[j]!=1){
				temp=b[j]-f[i];
				if(temp>=0){
					ff[i]=j;
					break;
				}
			}

		frag[i]=temp;
		bf[ff[i]]=1;
	}

	printf("\nFile_no\t\tFile_size\tBlock_no\tBlock_size\tFragement\n");
	for(i=1;i<=nf;i++)
		printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n",i,f[i],ff[i],b[ff[i]],frag[i]);
	exit(0);
}
