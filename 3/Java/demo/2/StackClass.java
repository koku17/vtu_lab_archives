// Program 13: To demonstrate Stack class

import java.util.Stack;

public class StackClass{
	public static void main(String[] args){
		Stack s=new Stack();
		s.push("Shreyas");
		s.push("Ramesh");
		s.push("Tom");
		System.out.println(s.pop()); // Tom
		System.out.println(s.pop()); // Ramesh
	}
}
