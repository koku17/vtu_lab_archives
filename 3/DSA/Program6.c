#include<stdio.h>
#include<stdlib.h>

#define max 10

int q[10],front=0,rear=-1,a;

void insert(){
	if((front==0&&rear==max-1)||(front>0&&rear==front-1))
		printf("Queue is overflow !\n");
	else{
		printf("Enter element to be insert : ");
		scanf("%d",&a);
		if(rear==max-1&&front>0){
			rear=0;
			q[rear]=a;
		}else if((front==0&&rear==-1)||(rear!=front-1))
			q[++rear]=a;
	}
}

void delete(){
	if((front==0)&&(rear==-1)){
		printf("Queue is underflow !\n");
		exit(1);
	}
	if(front==rear){
		a=q[front];
		rear=-1;
		front=0;
	}else if(front==max-1){
		a=q[front];
		front=0;
	}else
		a=q[front++];
	
	printf("Deleted element is : %d\n",a);
}

void display(){
	int i,j;
	if(front==0&&rear==-1){
		printf("Queue is underflow !\n");
		exit(1);
	}
	if(front>rear){
		for(i=0;i<=rear;i++)
			printf("%d ",q[i]);
		for(j=front;j<=max-1;j++)
			printf("%d ",q[j]);
	}else{
		for(i=front;i<=rear;i++)
			printf("%d ",q[i]);
	}
		
	printf("\nRear is at %d",q[rear]);
	printf("\nFront is at %d\n",q[front]);
}

void main(){
	int ch;
	
	printf("\nCircular Queue operations\n");
	printf("1. Insert\n2. Delete\n3. Display\n4. Exit\n");
	
	while(1){
		printf("\nEnter your choice : ");
		scanf("%d",&ch);
		
		switch(ch){
			case 1:
				insert();
				break;
			case 2:
				delete();
				break;
			case 3:
				display();
				break;
			case 4:
				exit(1);
			default:
				printf("Invalid option !\n");
		}
	}
}

