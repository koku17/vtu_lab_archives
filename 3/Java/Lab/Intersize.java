public interface Intersize{
	void resizeWidth(int width);
	void resizeHeight(int height);
}

class Rectangle implements Intersize{
	private int width,height;

	public Rectangle(int width,int height){
		this.width=width;
		this.height=height;
	}

	public void resizeWidth(int width){
		this.width=width;
	}
	
	public void resizeHeight(int height){
		this.height=height;
	}

	public void display(){
		System.out.println("The width is : "+width+"\nThe height is : "+height);
	}
}
