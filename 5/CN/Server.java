import java.io.*;
import java.net.*;

public class Server {
	public static void main (String[] args) throws Exception {
		DatagramSocket serverSocket = new DatagramSocket (9876);
		byte[] receivebuffer = new byte[1024];
		byte[] sendbuffer = new byte[1024];
		System.out.println ("Waiting for client request !");
		DatagramPacket recvdpkt = new DatagramPacket (receivebuffer, 0, receivebuffer.length);
		serverSocket.receive (recvdpkt);
		InetAddress IP = recvdpkt.getAddress ();
		int portno = recvdpkt.getPort ();
		System.out.println ("Connected to Client " + IP );
		String clientdata = new String (recvdpkt.getData (), recvdpkt.getOffset (), recvdpkt.getLength ());
		System.out.println ("\nClient Message : " + clientdata);
		System.out.print ("\nServer : ");
		BufferedReader serverRead = new BufferedReader (new InputStreamReader (System.in) );
		String serverdata = serverRead.readLine ();
		System.out.println ("\nServer sending ...");
		sendbuffer = serverdata.getBytes ();
		DatagramPacket sendPacket = new DatagramPacket (sendbuffer, sendbuffer.length, IP, portno);
		serverSocket.send (sendPacket);
		System.out.println ("Message sent to client !");
		serverSocket.close ();
	}
}
