#include <stdio.h>
#include <stdlib.h>
#include <string.h>

size_t bs=256;

typedef struct day{
    char *day,*AD;
    int d,m,y;
}Day;

void create(Day *cal){
        char *Days[]= \
                {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"};
        for(int i=0;i<7;i++){
                cal[i].day=strdup(Days[i]);
                cal[i].AD=(char *)malloc(bs*sizeof(char));
        }
}

void read(Day *cal){
        for(int i=0;i<7;i++){
                printf("Enter date for %s in dd/mm/yy : ",cal[i].day);
                scanf("%d%d%d",&cal[i].d,&cal[i].m,&cal[i].y);
                printf("Enter activity for %s : ",cal[i].day);
                while(getchar()!='\n')
                    ;
                getline(&cal[i].AD,&bs,stdin);
        }
}

void display(Day *cal){
        printf("%-10s %-10s \t %s\n","Day","Date","Activity");
        for(int i=0;i<7;++i){
                printf("%-10s %d/%d/%d \t %s\n", \
                        cal[i].day,cal[i].d, \
                        cal[i].m,cal[i].y, \
                        cal[i].AD
                );
        }
}

int main(){
        Day *cal=(Day *)malloc(7*sizeof(Day));
        if(cal==NULL){
                fprintf(stderr,"Memory allocation failed\n");
                return 1;
        }

        create(cal);
        read(cal);
        display(cal);

        for(int i=0;i<7;++i){
                free(cal[i].day);
                free(cal[i].AD);
        }
        free(cal);
        return 0;
}
