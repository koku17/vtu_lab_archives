public class CustomException{
	public static void main(String[] args){
		int a=25,b=0;
		try{
			if(b==0)
				throw new ArithmeticException("Divizion by 0 error");
			int result=a/b;
			System.out.println(a + "/" + b + "=" + result);
		}catch(ArithmeticException e){
			System.out.println("Raised exception is " + e);
		}finally{
			System.out.println("Execution Finished");
		}
	}
}
