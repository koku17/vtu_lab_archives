package Program2;

// Program 2: That contains the Scanner class to read Input
import java.util.*;

// Program to read from console using Scanner class and display output
public class Program2{
	public static void main(String[] args) {
		String qq;
		System.out.println("Enter your name");
		Scanner s=new Scanner(System.in);
		qq=s.nextLine();
		System.out.println(qq);
		s.close();
	}
}
