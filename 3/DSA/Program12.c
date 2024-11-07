#include<stdio.h>
#include<stdlib.h>

int key[20],n,m,*ht,ind,i,count=0;

void insert(int key){
	ind=key%m;
	while(ht[ind]!=-1)
		ind=(ind+1)%m;
	ht[ind]=key;
	count++;
}

void display(){
	if(count==0){
		printf("\nHash Table is empty !\n");
		exit(0);
	}

	printf("\nHash Table contents are :\n");
	for(i=0;i<m;i++)
		printf("\n T[%d] --> %d ",i,ht[i]);
	printf("\n");
	printf("Total records Inserted : %d\n",count);
}

void main(){
	printf("\nEnter the number of employee records (N) : ");
	scanf("%d",&n);

	printf("\nEnter the two digit memory locations (m) for hash table : ");
	scanf("%d",&m);
	ht=(int *)malloc(m*sizeof(int));

	for(i=0;i<m;i++)
	ht[i]=-1;

	printf("\nEnter the four digit key values (K) for N Employee Records :\n");
	for(i=0;i<n;i++)
		scanf("%d",&key[i]);

	for(i=0;i<n;i++){
		if(count==m){
			printf("\nHash table is full ! Cannot insert the record %d key",i+1);
			break;
		}
		insert(key[i]);
	}
	display();	
}
