#include<stdio.h>
#include<stdlib.h>

int n=0,count=0;
typedef struct node{
	char ssn[12],name[20],dept[25],desig[20];
	unsigned long long int phno;
	float sal;
	struct node *prev,*next;
}*NODE;

NODE x,temp,FIRST=NULL,END=NULL;

NODE getnode(){
	x=(NODE)malloc(sizeof(struct node));
	x->prev=x->next=NULL;
	return x;
}

void read(){
	temp=getnode();
	printf("Enter SSN : ");
	scanf("%s",temp->ssn);
	printf("Enter Name :\n");
	scanf("%s",temp->name);
	printf("Enter Department : ");
	scanf("%s",temp->dept);
	printf("Enter Designation : ");
	scanf("%s",temp->desig);
	printf("Enter Phone : ");
	scanf("%llu",&temp->phno);
	printf("Enter Salary : ");
	scanf("%f",&temp->sal);
}

void Insertionend(){
	printf("Enter the details of the employee\n");
	read();
	if(FIRST==NULL)
		FIRST=END=temp;
	else{
		END->next=temp;
		temp->prev=END;
		END=temp;
	}
}

void Create_DLL(){
	printf("Enter the number of Employees : ");
	scanf("%d",&n);
	while(n>0)
		Insertionend();
}

void display_count(){
	temp=FIRST;
	if(FIRST==NULL)
		printf("The Employee detail is NULL and count is %d\n",count);
	else{
		printf("Employee details:\n");
		printf("SSN \tEMPLOYEE NAME\tDEPARTMENT\tDESIGNATION\tPHONE NUMBER\tSALARY");
		while(temp!=NULL){
			count++;
			printf("\n%s\t%s\t%s\t\t%s\t\t%llu\t\t%0.2f",\
				temp->ssn,temp->name,temp->dept,temp->desig,temp->phno,temp->sal);
			temp=temp->next;
		}
			printf("\n Employee count is %d\n",count);
	}
}

void Insertionfront(){
	printf("Enter the details of the employee\n");
	read();
	if(FIRST==NULL)
		FIRST=END=temp;
	else{
		temp->next=FIRST;
		FIRST->prev=temp;
		FIRST=temp;
	}
}

void Deletionfront(){
	temp=FIRST;
	if(FIRST==NULL)
		printf("List is empty !\n");
	else{
		printf("Deleted element is %s\n",temp->ssn);
		count--;
		if(FIRST==END)
			FIRST=END=NULL;
		else{
			FIRST=FIRST->next;
			FIRST->prev=NULL;
		}
		free(temp);
	}
}

void Deletionend(){
	temp=END;
	if(FIRST==NULL)
		printf("List is empty !\n");
	else{
		printf("Deleted element is %s\n",temp->ssn);
		count--;
		if(FIRST==END)
			FIRST=END=NULL;
		else{
			END=END->prev;
			END->next=NULL;
		}
		free(temp);
	}
}

int main(){
	int choice;
		printf("\n1.Create DLL of N Employees \
			\n2.Display DLL \
			\n3.Insertion at front \
			\n4.Insertion at end \
			\n5.Deletion at front \
			\n6.Deletion at end \
			\n7.Exit\n"
		);
	while(1){
		printf("\n> ");
		scanf("%d",&choice);
			switch(choice){
				case 1 :
					Create_DLL();
					break;
				case 2:
					display_count();
					break;
				case 3:
					Insertionfront();
					break;
				case 4:
					Insertionend();
					break;
				case 5:
					Deletionfront();
					break;
				case 6:
					Deletionend();
					break;
				case 7:
					exit(0);
					break;
				default: printf("Invalid Choice !\n");
			}
	}
}
