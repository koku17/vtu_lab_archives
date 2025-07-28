package Program12;
import java.util.ArrayList;

public class Program12{
	public static void main(String[] args){
		ArrayList al=new ArrayList();
		al.add("Hacker");
		al.add("Anonymous");
		al.add("Richard Stallman");
		al.add("Linus Torvalds");
		for(int i=0;i<al.size();i++)
			System.out.println(al.get(i));
	}
}
