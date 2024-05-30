public class Abstract{
	public static void main(String[] args){
		Circle_S circle=new Circle_S(5.0);
		Triangle_S triangle=new Triangle_S(3.0,4.0,5.0);

		System.out.println("The area of the Circle is : "+circle.calculateArea());
		System.out.println("The perimeter of the Circle is : "+circle.calculatePerimeter());
		
		System.out.println("The area of the Triangle is : "+triangle.calculateArea());
		System.out.println("The perimeter of Triangle the is : "+triangle.calculatePerimeter());
	}
}
