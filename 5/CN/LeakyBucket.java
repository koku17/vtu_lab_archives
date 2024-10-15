import java.util.Scanner;
import java.lang.*;

public class LeakyBucket {
	public static void main (String[] args) {
		int i, buck_rem = 0, buck_cap = 4, rate = 3, sent, recv;
		int a[] = new int[20];
		Scanner in = new Scanner (System.in);
		System.out.print ("Enter the number of packets : ");
		int n = in.nextInt ();
		System.out.print ("\nEnter the packets : ");

		for (i = 1; i <= n; i++)
			a[i] = in.nextInt ();

		System.out.println ("\nClock \t packet size \t accept \t sent \t remaining");

		for (i = 1; i<=n; i++) {
			if (a[i] != 0) {
				if (buck_rem + a[i] > buck_cap)
					recv = -1;
				else {
					recv = a[i];
					buck_rem += a[i];
				}
			} else
				recv = 0;

			if (buck_rem != 0) {
				if (buck_rem < rate) {
					sent = buck_rem;
					buck_rem = 0;
				} else {
					sent = rate;
					buck_rem = buck_rem - rate;
				}
			} else
				sent = 0;

			if (recv == -1)
				System.out.printf("%3d \t %6d \t dropped \t %2d \t %5d\n", i, a[i], sent, buck_rem);
			else
				System.out.printf("%3d \t %6d \t %4d \t\t %2d \t %5d\n", i, a[i], recv, sent, buck_rem);
		}
	}
}
