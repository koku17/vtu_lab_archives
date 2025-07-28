public class Interface{
	public static void main(String[] args){
		Rectangle r=new Rectangle(20,30);

		System.out.println("The Original Rectangle");
		r.display();
		r.resizeWidth(40);
		r.resizeHeight(50);

		System.out.println("\nThe Resized Rectangle");
		r.display();
	}
}
