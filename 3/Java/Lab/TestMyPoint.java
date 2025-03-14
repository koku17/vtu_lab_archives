/*						Program 4
 * A class called MyPoint,which models a 2D point with x and y coordinates,is designed as follows:
 	- Two instance variables x(int) and y(int). 
	- A default(or "no-arg") constructor that construct a point at the default location of(0,0). 
	- A overloaded constructor that constructs a point with the given x and y coordinates. 
	- A method setXY() to set both x and y. 
	- A method getXY() which returns the x and y in a 2-element int array. 
	- A toString() method that returns a string description of the instance in the format "(x,y)". 
	- A method called distance(int x,int y) that returns the distance from this point to another point at
		the given(x,y) coordinates 
	- An overloaded distance(MyPoint another) that returns the distance from this point to the given MyPoint
		instance(called another) 
	- Another overloaded distance() method that returns the distance from this point to the origin(0,0)

* Develop the code for the class MyPoint. Also develop a JAVA program(called TestMyPoint) to test all the
	methods defined in the class. 
*/

class MyPoint{
	private int x;
	private int y;

	// Default constructor
	public MyPoint(){
		x=0;
		y=0;
	}
	// Overloaded constructor
	public MyPoint(int x,int y){
		this.x=x;
		this.y=y;
	}
	// Setter method to set both x and y
	public void setXY(int x,int y){
		this.x=x;
		this.y=y;
	}

	// Getter method to return x and y as a 2-element int array
	public int[] getXY(){
		int[] coordinates={x,y};
		return coordinates;
	}

	// Method to calculate distance to another point (x,y)
	public double distance(int x,int y){
		int dx=this.x-x;
		int dy=this.y-y;
		return Math.sqrt(dx*dx+dy*dy);
	}

	// Overloaded method to calculate distance to another MyPoint
	public double distance(MyPoint another){
		int dx=this.x-another.x;
		int dy=this.y-another.y;
		return Math.sqrt(dx*dx+dy*dy);
	}

	// Overloaded method to calculate distance to the origin (0,0)
	public double distance(){
		return Math.sqrt(x*x+y*y);
	}

	// toString method to provide a string representation of the point
	@Override
	public String toString(){
		return "("+x+","+y+")";
	}
}

public class TestMyPoint{
	public static void main(String[] args){
		// Create MyPoint instances
		MyPoint point1=new MyPoint();
		MyPoint point2=new MyPoint(3,4);

		// Test setXY and getXY methods
		point1.setXY(1,2);
		int[] coordinates=point1.getXY();
		System.out.println("Coordinates of point1 : ("+coordinates[0]+","+coordinates[1]+")");

		// Test distance methods
		double distance1=point1.distance(5,6);
		System.out.println("Distance from point1 to (5,6) : "+distance1);

		double distance2=point1.distance(point2);
		System.out.println("Distance from point1 to point2 : "+distance2);

		double distance3=point2.distance();
		System.out.println("Distance from point2 to the origin : "+distance3);

		// Test toString method
		System.out.println("Point1 : "+point1.toString());
		System.out.println("Point2 : "+point2.toString());
	}
}

