#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define FILES 5
#define NAME 20

typedef struct{
	char name[NAME];
	int size;
}file;

typedef struct{
	char name[NAME];
	int file_total;
	file files[FILES];
}dir;

dir sld,tld[FILES];

void init_SLD(){
	strcpy(sld.name,"Root");
	sld.file_total=0;
}

void init_TLD(){
	for(int i=0;i<FILES;++i){
		sprintf(tld[i].name,"Directory%d",i+1);
		tld[i].file_total=0;
	}
}

void display_SLD(){
	printf("Single Level Directory :\nDirectory Name : %s\nNumber of Files : %d\n", \
		sld.name,sld.file_total \
	);

	printf("Files :\n");

	for(int i=0;i<sld.file_total;++i){
		printf( \
			"File Name : %s, Size : %d KB\n", \
			sld.files[i].name,sld.files[i].size
		);
	}
	printf("\n");
}

void display_TLD(){
	printf("Two Level Directory:\n");
	for(int i=0;i<FILES;++i){
		printf( \
			"Directory Name : %s\nNumber of Files : %d\nFiles :\n", \
			tld[i].name,tld[i].file_total
		);
		for(int j=0;j<tld[i].file_total;++j){
			printf( \
				"File Name : %s, Size : %d KB\n", \
				tld[i].files[j].name,tld[i].files[j].size
			);
		}
		printf("\n");
	}
}

void add_file_SLD(char name[],int size){
	if(sld.file_total<FILES){
		strcpy(sld.files[sld.file_total].name,name);
		sld.files[sld.file_total].size=size;
		sld.file_total++;
		printf("File '%s' added to Single Level Directory\n",name);
	}else
		printf("Single Level Directory is full,cannot add file '%s'\n",name);
}

void add_file_TLD(char name[],int size,int index){
	if(index>=0 && index<FILES)
		if(tld[index].file_total<FILES){
			strcpy(tld[index].files[tld[index].file_total].name,name);
			tld[index].files[tld[index].file_total].size=size;
			tld[index].file_total++;
			printf( \
				"File '%s' added to Directory '%s'\n", \
				name,tld[index].name
			);
		}else
			printf( \
				"Directory '%s' is full,cannot add file '%s'\n", \
				tld[index].name,name
			);
	else
		printf("Invalid Directory Index for Two Level Directory\n");
}

int main(){
	init_SLD();
	init_TLD();
	add_file_SLD("file1.txt",1024);
	add_file_SLD("file2.txt",2048);
	add_file_SLD("file3.txt",3072);
	display_SLD();
	add_file_TLD("file4.txt",4096,0);
	add_file_TLD("file5.txt",5120,1);
	add_file_TLD("file6.txt",6144,2);
	display_TLD();
	return 0;
}
