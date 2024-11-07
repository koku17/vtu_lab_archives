package Program14;

public class Program14{
	public static void main(String[] args){
		int a,b,c,n;
		a=b=c=n=1;
		while(n<=10){
			System.out.print(" "+a);
			c=a+b;
			a=b;
			b=c;
			n++;
		}
	}
}
