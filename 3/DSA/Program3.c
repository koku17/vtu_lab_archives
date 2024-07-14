#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define max_size 5

int stack[max_size],top=-1,i,item;

void push(){
	if(top==(max_size-1))
		printf("\nStack Overflow !");
	else{
		printf("Enter the element to be inserted : ");
		scanf("%d",&item);
		stack[++top]=item;
	}
}

void pop(){
	if(top==-1)
		printf("Stack Underflow !\n");
	else
		printf("\nThe poped element : %d\n",stack[top--]);
}

void pali(){
	if(top==-1)
		printf("Push some elements into the stack first !\n");
	else
		for(i=top;i>=0;i--)
			if(stack[i]!=stack[top-i]){
				printf("Not Palindrome\n");
				return;
			}

	printf("Palindrome !\n");
}

void display(){
	if(top==-1)
		printf("Stack is Empty !\n");
	else{
		printf("The stack elements are : ");
		for(i=top;i>=0;i--)
			printf("%d ",stack[i]);
		printf("\n");
	}
}

int main(){
	int choice;
	printf("\n\n--------STACK OPERATIONS--------\n");
	printf("1.Push\n2.Pop\n3.Palindrome\n4.Display\n5.Exit\n");
	while(1){
		printf("> ");
		scanf("%d",&choice);
		switch(choice){
			case 1:
				push();
				break;
			case 2:
				pop();
				break;
			case 3:
				pali();
				break;
			case 4:
				display();
				break;
			case 5:
				exit(0);
				break;
			
			default:
				printf("\nInvalid choice !");
				break;
		}
	}
}
