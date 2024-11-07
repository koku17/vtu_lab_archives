package Program8;

// Program 8 - To demonstrate Type Casting in Java

/* Two types of casting
 * Widening Casting (automatically) - converting a smaller type to a larger type size
 * byte -> short -> char -> int -> long -> float -> double

 * Narrowing Casting (manually) - converting a larger type to a smaller size type
 * double -> float -> long -> int -> char -> short -> byte
 */

public class Program8{
	public static void main(String[] args){
    		// Widening casting example
		int myInt=9;
		double myDouble=myInt;		// Automatic casting: int to double

		System.out.println(myInt);	// Outputs 9
		System.out.println(myDouble);   // Outputs 9.0

		// Narrowing casting example - Truncate
		double mydbl=9.78;
	    	int myIn=(int) mydbl;		// Manual casting: double to int
		
		System.out.println(mydbl);	// Outputs 9.78
		System.out.println(myIn);	// Outputs 9
	}

}
