/*
 *				Program 2
 * Develop a stack class to hold a maximum of 10 integers with suitable methods
 * Develop a java class method to illustrate stack operation
 */

package stackop;

public class StackOp{
	private int[] stackArray;
	private int top;
	private static final int MAX_SIZE=10;

	public StackOp(){
		stackArray=new int[MAX_SIZE];
		top=-1;
	}

	public void push(int data){
		if(isFull())
			System.out.println(data+" : Stack is full, cannot Push");
		else{
			stackArray[++top]=data;
			System.out.println(data+" : Pushed on to the Stack");
		}
	}

	public int pop(){
		if(isEmpty()){
			System.out.println("Stack is empty, cannot Pop !");
			return -1;
		}else{
			int poppedItem=stackArray[top--];
			System.out.println(poppedItem+" : Popped from the Stack");
			return poppedItem;
		}
	}

	public boolean isEmpty(){
		return top==-1;
	}

	public boolean isFull(){
		return top==MAX_SIZE-1;
	}

	public static void main(String[] args){
		StackOp stack=new StackOp();
		for(int i=0;i<=10;i++)
			stack.push(5*i);

		System.out.println("Is the Stack empty ? "+stack.isEmpty());
		System.out.println("Is the Stack full ? "+stack.isFull());

		System.out.println("\nPopping elements from the Stack :");
		while(!stack.isEmpty())
			stack.pop();

		System.out.println("Is the Stack empty ? "+stack.isEmpty());
		System.out.println("Is the Stack full ? "+stack.isFull());

		System.out.println("\nPopping elements from the Stack :");
		while(!stack.isEmpty())
			stack.pop();

		System.out.println("Is the Stack empty ? "+stack.isEmpty());
		System.out.println("Is the Stack full ? "+stack.isFull());
	}
}
