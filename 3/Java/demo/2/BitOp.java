// Program to demonstrate Bitwise operations in Java

public class BitOp{
	public static void main(String[] args){
		String binary[]={"0000","0001","0010","0011","0100","0101","0110","0111","1000","1001",
		"1010", "1011","1100","1101","1110","1111"};

		int a=3;
		int b=6;
		int c=a|b;
		int d=a&b;
		int e=a^b;
		int f=(~a&b)|(a&~b);
		System.out.println("a or b  :  "+binary[c]);		// 1 if either is 1 or both 1
		System.out.println("a and b :  "+binary[d]);		// 1 if both 1
		System.out.println("a xor b :  "+binary[e]);		// 1 if either value is 1
									// 0 for both 0 or both 1
		System.out.println("(~a&b)|(a & ~b) :  "+binary[f]);	// ~ is NOT ; ~a=1100
	}
}
