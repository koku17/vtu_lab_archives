package Program9;

// Java Operators
public class Program9{
	public static void main(String[] args){
		// Arithmetic Operators +, -, *, /, % (modulus), ++ (increment), -- (decrement)
		int x=10;
		int y=4;
		System.out.println(x % y);	// 2
		++x;
		System.out.println(x);		// 11

		// Addition Assignment Operator
		x+=5;
		System.out.println(x);		// 16
     
		// Comparison Operators < , >, <=, >=, ==, !=
		System.out.println(x!=y);	//returns true
		    
		// Logical Operators && (logical And), || (Logical Or), ! (Logical Not)
		System.out.println(x>3&&x<10);		// returns false
		System.out.println(x<3||x>10);		// returns true 
		System.out.println(!(x<3||x>10));	// returns false
	}
}
