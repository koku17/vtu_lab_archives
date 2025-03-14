package MyPack;
class MyClass{
	public void displayMessage(){
		System.out.println("This is a message from the MyClass in mypack package.");
	}
}

public class MainApp{
	public static void main(String[] args){
		MyClass myObject=new MyClass();
		myObject.displayMessage();
	}
}
