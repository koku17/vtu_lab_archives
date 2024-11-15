import java.util.Scanner;

class CRC {
	public static void main (String args[]) {
		Scanner sc = new Scanner (System.in);
	
		System.out.print ("Enter data stream : ");
		String datastream = sc.nextLine ();
		System.out.print ("Enter generator : ");
		String generator = sc.nextLine ();
	
		int data[] = new int[datastream.length () + generator.length () - 1];
		int divisor[] = new int[generator.length ()];

		for (int i = 0; i < datastream.length (); i++)
			data[i] = Integer.parseInt (datastream.charAt (i) + "");

		for (int i = 0; i < generator.length (); i++)
			divisor[i] = Integer.parseInt (generator.charAt (i) + "");

		for (int i = 0; i < datastream.length (); i++)
			if (data[i] == 1)
				for (int j = 0; j < divisor.length; j++)
					data[i + j] ^= divisor[j];

		System.out.print ("The CRC code is : ");

		for (int i = 0; i < datastream.length (); i++)
			data[i] = Integer.parseInt (datastream.charAt (i) + "");

		for (int i = 0; i < data.length; i++)
			System.out.print (data[i]);

		System.out.println ();
		System.out.print ("Enter CRC code : ");
		datastream = sc.nextLine ();
		System.out.print ("Enter generator : ");
		generator = sc.nextLine ();
		data = new int[datastream.length () + generator.length () - 1];
		divisor = new int[generator.length ()];

		for (int i = 0; i < datastream.length (); i++)
			data[i] = Integer.parseInt (datastream.charAt (i) + "");

		for (int i = 0; i < generator.length (); i++)
			divisor[i] = Integer.parseInt (generator.charAt (i) + "");

		for (int i = 0; i < datastream.length (); i++)
			if (data[i] == 1)
				for (int j = 0; j < divisor.length; j++)
					data[i + j] ^= divisor[j];

		boolean valid = true;

		for (int i = 0; i < data.length; i++)
			if (data[i] == 1) {
				valid = false;
				break;
			}

		if (valid == true)
			System.out.println ("Data stream is valid");
		else
			System.out.println ("Data stream is invalid !\nCRC error occured");
	}
}
