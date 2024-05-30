class MyRunnable implements Runnable{
	public void run(){
		try{
			Thread.sleep(500);
			System.out.println("Thread ID : "+Thread.currentThread().getId()+" is running !");
		}catch(InterruptedException e){
			System.out.println("Thread Interrupted : "+e.getMessage());
		}
	}
}

public class MainThreads{
	public static void main(String[] args){
		Thread thread1=new Thread(new MyRunnable());
		Thread thread2=new Thread(new MyRunnable());
		Thread thread3=new Thread(new MyRunnable());

		thread1.start();
		thread2.start();
		thread3.start();
	}
}
