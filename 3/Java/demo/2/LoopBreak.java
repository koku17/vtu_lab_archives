// Program to demonstrate for loop, break and continue in java

public class LoopBreak{
	public static void main(String[] args){
			for(int i=0;i<4;i++)
				System.out.println("Hello");

			// demonstrate break in java
			// Exits the loop when the condition is reached
			for(int i=0;i<4;i++){
				if(i==3){
					System.out.println("Number 3");
					break;
				}
				else
					System.out.println("Other Number");
			}

			// demonstrate continue in java
			// The continue statement breaks one iteration (in the loop),
			// if a specified condition occurs, and continues with the next
			// iteration in the loop.

			for(int i=0;i<10;i++){
				if (i==4)
					continue;
				System.out.println(i);
	}
	}
}
