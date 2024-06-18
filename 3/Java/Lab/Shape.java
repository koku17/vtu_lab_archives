public class Shape{
	void draw(){
		System.out.println("Draw a Shape\n");
	}
	
	void erase(){
		System.out.println("Erase a Shape\n");
	}

	public static void main(String[] args){
		Shape s1=new Circle();
		s1.draw();
		s1.erase();
		
		Shape s2=new Triangle();
		s2.draw();
		s2.erase();
		
		Shape s3=new Square();
		s3.draw();
		s3.erase();
	}
}
