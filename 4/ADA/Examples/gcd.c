#include<stdio.h>
#include<stdlib.h>

int i,m,n,n1,n2,result,T;

// Euclidean GCD Algorithm
int euclid_gcd(int dividend,int divisor){
	if(dividend%divisor==0)
		return divisor;
	else
		return euclid_gcd(divisor,dividend%divisor);
}

// Mid School GCD Algorithm
int midschool_gcd(int m,int n){
	while(i<=(m<n?m:n))
		if(m%i==0 && n%i==0)
			return i;
		else
			i--;
	return 1;
}

// Consecutive Integer Checking Algorithm
int cic_gcd(int n1,int n2){
	m=n1>n2?n1:n2;
	n=T=n1<n2?n1:n2;
	while(m%T!=0||n%T!=0)
		T--;
	return T;
}

void help(){
	printf("Usage:gcd [option] [num1] [num2] \
		\n Options: \
		\n\t  e Use Euclidean GCD Algorithm \
		\n\t  m Use Mid School GCD Algorithm \
		\n\t  c Use Consecutive Integer Checking Algorithm \
		\n\t  h Display this help message \n" \
	);
}

int main(int argc,char *argv[]){
	for(i=1;i<argc;i++){
		if(*argv[i] == 'e'){
				printf("Euclidean Algorithm :\n");
				n1=atoi(argv[++i]);
				n2=atoi(argv[++i]);
				result=euclid_gcd(n1,n2);
		}else if(*argv[i] == 'm'){
				printf("Mid-School Algorithm :\n");
				n1=atoi(argv[++i]);
				n2=atoi(argv[++i]);
				result=midschool_gcd(n1,n2);
		}else if(*argv[i] == 'c'){
				printf("CIC Algorithm :\n");
				n1=atoi(argv[++i]);
				n2=atoi(argv[++i]);
				result=cic_gcd(n1,n2);
		}else{
			help();
		}
		printf("GCD(%d,%d) = %d\n",n1,n2,result);
	}
	return EXIT_SUCCESS;
}
