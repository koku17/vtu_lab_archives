// Program to generate Fibonacci series

public class Fibonacci{
	public static void main(String[] args){
		int a,b,c,n;
		a=b=n=1;
		while(n<=10){
			System.out.print(" "+a);
			c=a+b;
			a=b;
			b=c;
			n++;
		}
	}
}
