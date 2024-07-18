#include<stdlib.h>
#include<stdio.h>
#include<time.h>

int i,j,n,pivot,pi,temp;

int partition(int arr[],int low,int high){
	pivot=arr[high];
	i=(low-1);
	for(j=low;j<high;j++)
		if(arr[j]<= pivot){
			i++;
			temp=arr[i];
			arr[i]=arr[j];
			arr[j]=temp;
		}
	temp=arr[i+1];
	arr[i+1]=arr[high];
	arr[high]=temp;
	return i+1;
}

void quickSort(int arr[],int low,int high){
	if(low<high){
		pi=partition(arr,low,high);
		quickSort(arr,low,pi-1);
		quickSort(arr,pi+1,high);
	}
}

int main(int argc,char *argv[]){
	for(i=1;i<argc;i++){
		n=atoi(argv[i]);
		if(n==1){
			printf("Time taken to sort %d elements is %f seconds\n",1,0.000001);
			return 0;
		}
		int arr[n];
		srand(time(0));
		for(i=0;i<n;i++)
			arr[i]=rand()%10000;
		clock_t start=clock();
		quickSort(arr,0,n-1);
		clock_t end=clock();
		double time_taken=((double)(end-start))/CLOCKS_PER_SEC;
		printf("Time taken to sort %d elements is %f seconds\n",n,time_taken*1000);
	}
	return 0;
}
