import java.util.Scanner;

public class RSA {
	int d, e, n;
	String M;

	int gcd (int m, int n) {
		int rv = n == 0 ? m : gcd (n, m % n);
		return rv;
	}

	int pow (int a, int m, int n) {
		int r = 1;

		while (m-- != 0)
			r = (r * a) % n;

		return r;
	}

	void rsa () {
		int p = 11, q = 13, z;

		n = p * q;
		z = (p - 1) * (q - 1);

		for (e = 2; gcd (e, z) != 1; e++)
			;

		for (d = 2; (d * e) % z != 1; d++)
			;
	}

	void input () {
		Scanner scanner = new Scanner (System.in);
		System.out.print ("Enter M : ");
		M = scanner.next ();
		scanner.close ();
	}

	void output () {
		System.out.println ("S = (d, n) = (" + d + ", " + n + ")");
		System.out.println ("P = (e, n) = (" + e + ", " + n + ")\n");
		System.out.println ("T : " + M);

		char[] T = M.toCharArray ();

		for (int i = 0; i < M.length (); i++)
			T[i] = (char) pow ((int) T[i], e, n);

		System.out.println ("C : " + String.valueOf (T));

		for (int i = 0; i < M.length (); i++)
			T[i] = (char) pow ((int) T[i], d, n);

		System.out.println ("T : " + String.valueOf (T));
	}

	public static void main (String[] args) {
		RSA r = new RSA ();
		r.input ();
		r.rsa ();
		r.output ();
	}
}
