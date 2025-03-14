abstract class Abstract{
	void normal_method(){
		System.out.println("Normal method in Abstract class");
	}
}

class Normal extends Abstract{
	void normal(){
		System.out.println("Normal method in Normal class");
	}

}

public class AbstractExample{
	public static void main(String[] args){
		Normal obj=new Normal();
		
		obj.normal_method();
		obj.normal();
	}
}
