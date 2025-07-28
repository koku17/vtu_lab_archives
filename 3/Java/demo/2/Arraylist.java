// Program 12: To demonstrate Collections - ArrayList

import java.util.ArrayList;

public class Arraylist{
	public static void main(String[] args){
		ArrayList al = new ArrayList();
		al.add("Shreyas Rao");
		al.add("Rajesh");
		al.add("Karthik");
		al.add("Anusha");
				
		for(int i=0;i<al.size();i++)
			System.out.println(al.get(i));
	}
}
