class Outer{
	void display(){
		System.out.println("You are inside Outer class");
	}

	class inner{
		void display(){
			System.out.println("You are inside Inner class");
		}
	}
}

public class OuterClass{
	public static void main(String[] args){
		Outer out=new Outer();
		out.display();

		Outer.inner in=out.new inner();
		in.display();
	}
}
