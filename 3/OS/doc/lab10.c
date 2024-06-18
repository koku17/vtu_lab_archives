#include <stdio.h>
#include <stdlib.h>

int main(){
	int queue[20],head,n,i,j,seekTime=0,direction,maxTrack;

	printf("Enter the number of disk requests : ");
	scanf("%d",&n);

	printf("Enter the disk request queue : ");
	for(i=0;i<n;i++)
		scanf("%d",&queue[i]);

	printf("Enter the initial head position : ");
	scanf("%d",&head);

	printf("Enter the maximum track number : ");
	scanf("%d",&maxTrack);

	printf("Enter the direction(0 for left,1 for right) : ");
	scanf("%d",&direction);

	printf("\n");

	int temp;
	for(i=0;i<n-1;i++)
		for(j=i+1;j<n;j++)
			if(queue[i]>queue[j]){
				temp=queue[i];
				queue[i]=queue[j];
				queue[j]=temp;
			}

	int currentTrack=head;
	printf("Seek Sequence :\n");
	if(direction==0){
		for(i=head;i>=0;i--){
			printf("%d ",i);
			seekTime+=abs(currentTrack-i);
			currentTrack=i;
		}
		printf("\n\n0 ");
		seekTime+=currentTrack;

		for(i=1;i<=maxTrack;i++){
			printf("%d ",i);
			seekTime+=abs(currentTrack-i);
			currentTrack=i;
		}
		printf("\n\n");
	}else{
		for(i=head;i<=maxTrack;i++){
			printf("%d ",i);
			seekTime+=abs(currentTrack-i);
			currentTrack=i;
		}
		printf("\n\n%d ",maxTrack);
		seekTime+=abs(currentTrack-maxTrack);
		for(i=maxTrack-1;i>=0;i--){
			printf("%d ",i);
			seekTime+=abs(currentTrack-i);
			currentTrack=i;
		}
	}

	printf("\n\nTotal Seek Time : %d\n",seekTime);
	exit(0);
}
