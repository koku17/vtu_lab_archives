import java.util.*;

public class LeakyBucket {
	int n, burst, outgoingRate, bucketSize;
	int incoming, outgoing, pending, overflow;
	int duration, interval;

	LeakyBucket () {
		pending = incoming = overflow = outgoing = 0;
	}

	void leakyBucket () {
		System.out.println ("Time Incoming Pending Overflow Outgoing");
		Random rand = new Random ();

		int time = 0;

		while (time < duration) {
			incoming = rand.nextInt (burst);

			if ((pending + incoming) > bucketSize) {
				overflow = (pending + incoming) - bucketSize;
				pending = bucketSize;
			} else
				pending += incoming;

			interval = 1;

			for (int clk = 0; clk < interval; ++clk) {
				output (time, incoming, pending, overflow, outgoing);
				outgoing = Math.min (outgoingRate, pending);
				pending -= outgoing;
				incoming = 0;
				++time;
			}
		}
	}

	void input () {
		Scanner scanner = new Scanner (System.in);

		System.out.print ("Enter burst size : ");
		burst = scanner.nextInt ();

		System.out.print ("Enter bucket size : ");
		bucketSize = scanner.nextInt ();

		System.out.print ("Enter outgoing rate : ");
		outgoingRate = scanner.nextInt ();

		System.out.print ("Enter duration : ");
		duration = scanner.nextInt ();

		scanner.close ();
	}

	void output (int time, int incoming, int pending, int overflow, int outgoing) {
		System.out.printf ("%3d %6d %7d %7d %8d\n", time, incoming, pending, overflow, outgoing);
	}

	public static void main (String[] args) {
		LeakyBucket lb = new LeakyBucket ();
		lb.input ();
		lb.leakyBucket ();
	}
}
