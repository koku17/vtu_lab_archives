#include<stdlib.h>
#include<stdio.h>
#include<time.h>

int i,j,k,lb,mid,n,n1,n2,ub;

void merge(int arr[],int lb,int mid,int ub){
	n1=mid-lb+1;
	n2=ub-mid;

	int left[n1],right[n2];

	for(i=0;i<n1;i++)
		left[i]=arr[lb+i];
	for(j=0;j<n2;j++)
		right[j]=arr[mid+1+j];
	i=j=0;
	k=lb;
	while(i<n1&&j<n2)
		if(left[i]<=right[j])
			arr[k++]=left[i++];
		else
			arr[k++]=right[j++];

	while(i<n1)
		arr[k++]=left[i++];

	while(j<n2)
		arr[k++]=right[j++];
}

void mergeSort(int arr[],int lb,int ub){
	if(lb<ub){
		mid=lb+(ub-lb)/2;
		mergeSort(arr,lb,mid);
		mergeSort(arr,mid+1,ub);
		merge(arr,lb,mid,ub);
	}
}

int main(int argc,char *argv[]){
	for(int i=1;i<argc;i++){
		n=atoi(argv[i]);
    	int arr[n];
		srand(time(0));
		for(int j=0;j<n;j++)
			arr[j]=rand()%10000;
		clock_t start=clock();
		mergeSort(arr,0,n-1);
		clock_t end=clock();
		double time_taken=((double)(end-start))/CLOCKS_PER_SEC;
		printf("Time taken to sort %d elements is %f seconds\n",n,time_taken*1000);
	}
	return 0;
}
