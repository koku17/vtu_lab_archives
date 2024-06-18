package Program3;

// Program 3: To use if-else and find biggest of two numbers
import java.util.*;

public class Program3{
	public static void main(String[] args){
		int a,b,big;
		System.out.print("Enter the values for A and B\n> ");
		Scanner s=new Scanner(System.in);
		a=Integer.parseInt(s.nextLine());
		System.out.print("> ");
		b=Integer.parseInt(s.nextLine());
		if(a>b)
			big=a;
		else 
			big=b;
		System.out.println("Biggest is: "+ big);
	}
}
