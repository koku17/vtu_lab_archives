package Program13;
import java.util.Stack;

public class Program13{
	public static void main(String[] args){
		Stack s=new Stack();
		s.push("Unix sys V");
		s.push("Berkely Software Distribution");
		s.push("Linux");
		System.out.println(s.pop());
		System.out.println(s.pop());
	}
}
