#include<stdio.h>
#include<stdlib.h>

int i,j,m,n,n1,n2,result,T;

// Euclidean GCD Algorithm
int euclid_gcd(int dividend,int divisor){
	if(dividend%divisor==0)
		return divisor;
	else
		return euclid_gcd(divisor,dividend%divisor);
}

// Mid School GCD Algorithm
int midschool_gcd(int m,int n){
	i=m<n?m:n;
	while(i>=1)
		if(m%i==0&&n%i==0)
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

void help(char argv[]){
	printf("Usage : %s [option] [num1] [num2] \
		\n Options : \
		\n\t e Use Euclidean GCD Algorithm \
		\n\t m Use Mid School GCD Algorithm \
		\n\t c Use Consecutive Integer Checking Algorithm \
		\n\t h Display this help message and exit \n",argv \
	);
}

int main(int argc,char *argv[]){
	if(argc==1){
		help(argv[0]);
		exit(EXIT_SUCCESS);
	}
	for(j=1;j<argc;j++){
		switch(*argv[j]){
			case 'e':
				printf("Euclidean Algorithm :\n");
				n1=atoi(argv[++j]);
				n2=atoi(argv[++j]);
				result=euclid_gcd(n1,n2);
				break;
			case 'm':
				printf("Mid-School Algorithm :\n");
				n1=atoi(argv[++j]);
				n2=atoi(argv[++j]);
				result=midschool_gcd(n1,n2);
				break;
			case 'c':
				printf("CIC Algorithm :\n");
				n1=atoi(argv[++j]);
				n2=atoi(argv[++j]);
				result=cic_gcd(n1,n2);
				break;
			case 'h':
			default:
				help(argv[0]);
				return EXIT_SUCCESS;
		}
		printf("GCD(%d,%d) = %d\n",n1,n2,result);
	}
	return EXIT_SUCCESS;
}
