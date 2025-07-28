abstract class Shapes{
	abstract public double calculateArea();
	abstract public double calculatePerimeter();
}

class Circle_S extends Shapes{
	private double radius;
	
	public Circle_S(double radius){
		this.radius=radius;
	}

	@Override
	public double calculateArea(){
		return Math.PI*radius*radius;
	}
	
	@Override
	public double calculatePerimeter(){
		return 2*Math.PI*radius;
	}
}

class Triangle_S extends Shapes{
	private double side1,side2,side3;
	
	public Triangle_S(double side1,double side2,double side3){
		this.side1=side1;
		this.side2=side2;
		this.side3=side3;
	}

	@Override
	public double calculateArea(){
		double S=(side1+side2+side3)/2;
		return Math.sqrt(S*(S-side1)*(S-side2)*(S-side3));
	}
	
	@Override
	public double calculatePerimeter(){
		return side1+side2+side3;
	}
}
