#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

struct directory{
	char dname[10],fname[10][10];
	int fcnt;
}dir[10];

int main(){
	int i,ch,dcnt=0,k;
	char f[30],d[30];

	printf("\n1. Create Directory\n2. Create File\n3. Delete File\n4. Search File\n5. Display\n6. Exit\n");
	while(1){
		printf("\n> ");
		scanf("%d",&ch);
		switch(ch){
			case 1:
				printf("\nEnter name of directory : ");
				scanf("%s",dir[dcnt].dname);
				dir[dcnt].fcnt=0;
				dcnt++;
				printf("\nDirectory created !");
				break;
			case 2:
				printf("\nEnter name of the directory : ");
				scanf("%s",d);
				for(i=0;i<dcnt;i++)
					if(strcmp(d,dir[i].dname)==0){
						printf("Enter name of the file : ");
						scanf("%s",dir[i].fname[dir[i].fcnt]);
						dir[i].fcnt++;
						printf("\nFile created !");
					}

				if(i!=dcnt)
					printf("\nDirectory %s not found",d);
				break;
			case 3:
				printf("\nEnter name of the directory : ");
				scanf("%s",d);

				for(i=0;i<dcnt;i++)
					if(strcmp(d,dir[i].dname)==0){
						printf("Enter name of the file : ");
						scanf("%s",f);

						for(k=0;k<dir[i].fcnt;k++){
							if(strcmp(f,dir[i].fname[k])==0){
								printf("\nFile %s is deleted ",f);
								dir[i].fcnt--;
								strcpy(dir[i].fname[k],dir[i].fname[dir[i].fcnt]);
								goto jmp;
							}
						}

						printf("\nFile %s not found",f);
						goto jmp;
					}

				printf("\nDirectory %s not found",d);

				jmp:
				break;
			case 4:
				printf("\nEnter name of the directory : ");
				scanf("%s",d);

				for(i=0;i<dcnt;i++)
					if(strcmp(d,dir[i].dname)==0){
						printf("\nEnter the name of the file : ");
						scanf("%s",f);
						for(k=0;k<dir[i].fcnt;k++)
							if(strcmp(f,dir[i].fname[k])==0){
								printf("\nFile %s is found ",f);
								goto jmp1;
							}

						printf("\nFile %s not found",f);
						goto jmp1;
					}

				printf("\nDirectory %s not found",d);

				jmp1:
				break;
			case 5:
				if(dcnt==0)
					printf("\nNo Directories ");
				else{
					printf("\nDirectory\tFiles");

					for(i=0;i<dcnt;i++){
						printf("\n%s\t",dir[i].dname);
						for(k=0;k<dir[i].fcnt;k++)
							printf("\t%s",dir[i].fname[k]);
					}
				}
				break;
			default:
				exit(0);
		}
	}
}
