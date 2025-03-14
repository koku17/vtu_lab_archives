import java.util.Scanner;

public class CRC {
	int W;
	char[] P;
	String checksum, message;

	CRC () {
		W = 16;
		P = "10001000000100001".toCharArray ();
	}
	
	void crc () {
	String crc = "0000000000000000";
	char[] msg = (message + crc).toCharArray ();
	char[] rem = (crc + '0').toCharArray ();
	int n = 0;

	while (n < msg.length) {
		rem[W] = msg[n++];
		boolean xorcopy = rem[0] == '1';

		for (int i = 1; i <= W; i++)
			rem[i - 1] = xorcopy ? (rem[i] == P[i] ? '0' : '1') : rem[i];

		checksum = String.valueOf (rem).substring (0, W);
	}

	void input () {
		Scanner scanner = new Scanner (System.in);
		System.out.print ("MESSAGE : ");
		message = scanner.next ();
		scanner.close ();
	}

	void output () {
		System.out.println ("Checksum : " + checksum);
	}
	
	public static void main (String[] args) {
		CRC crc = new CRC ();
		crc.input ();
		crc.crc ();
		crc.output ();
	}
}
