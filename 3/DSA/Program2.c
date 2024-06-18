#include<stdio.h>

void main(){
	char STR[100],PAT[100],REP[100],ANS[100];
	int c,i,j,m,k,flag;
	printf("Enter the MAIN string : ");
	scanf("%[^\n]",STR);
	printf("Enter the PATTERN string : ");
	scanf("%s",PAT);
	printf("Enter the REPLACE string : ");
	scanf("%s",REP);
	c=i=j=m=k=flag=0;

	while(STR[c]!='\0'){
		if(STR[m]==PAT[i]){
			i++;
			m++;
			flag=1;
			if(PAT[i]=='\0'){
				for(k=0;REP[k]!='\0';j++,k++)
					ANS[j]=REP[k];
				i=0;
				c=m;
			}
		}else{
			ANS[j]=STR[c];
			j++;
			c++;
			m=c;
			i=0;
		}
	}

	if(flag){
		ANS[j]='\0';
		printf("\nThe resultant string is %s\n",ANS);
	}else
		printf("Pattern doesn't found !\n");
}
