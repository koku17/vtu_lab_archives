import java.util.Scanner;

public class SlidingWindow {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter window size : ");
		int w = scanner.nextInt();
		System.out.print("\nEnter number of frames to transmit : ");
		int f = scanner.nextInt();
		int[] frames = new int[f];
		System.out.print("\nEnter " + f + " frames :\n");

		for (int i = 0; i < f; i++)
			frames[i] = scanner.nextInt();

		System.out.println (
			"\nWith sliding window protocol the frames will be sent in the following manner " +
			"(assuming no corruption of frames)\n"
		);

		System.out.printf (
			"After sending %d frames at each stage sender waits for acknowledgement sent by the receiver\n\n", w
		);
		
		for (int i = 0; i < f; i++) {
			System.out.print(frames[i] + " ");

			if ((i + 1) % w == 0 || (i + 1) == f)
				System.out.printf ("\nAcknowledgement of above frames sent is received by sender\n\n");
		}
		scanner.close();
	}
}
