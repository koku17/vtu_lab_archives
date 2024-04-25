// Program to demonstrate return statement
class ReturnEx{
	public static void main(String[] args){
		boolean t=true;
		System.out.println("Before Return");
		if(t)
			return;
		System.out.println("After Return"); // Never executed
	}
}
