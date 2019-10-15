import java.net.*;
import java.io.*;
import java.util.*;
//-----------------VERY IMPORTANT-----------------------//
//---------------|||||||||||||||||||--------------------//
//---------------SERVER SHOULD CLOSE ONLY ON EXPLICIT CTRL+C------------//
public class BasicServer extends Thread{

	private ServerSocket serverSocket;
	Map<Integer,Integer> db = new HashMap<Integer,Integer>();
	public BasicServer(){
		try{
			serverSocket = new ServerSocket(5000);
			System.out.println("Listening on 5000");
		}
		catch (IOException e) {
            System.out.println("Exception caught when trying to listen on port "
                + "5000" + " or listening for a connection");
            System.out.println(e.getMessage());
        }
	}
	public void run(){
		while(true){
			try ( 
	            Socket clientSocket = serverSocket.accept();
	            PrintWriter out =
	                new PrintWriter(clientSocket.getOutputStream(), true);
	            BufferedReader in = new BufferedReader(
	                new InputStreamReader(clientSocket.getInputStream()));
	        ) {
	        	//System.out.println("connected to client");
	        	//System.out.println(in.readLine());
				String inputLine,outputLine;
	            while ((inputLine = in.readLine()) != null) {

	            	String[] arr = inputLine.split(" ");
	            	//System.out.println(inputLine);
	            	//System.out.println("yo");
	            	if(arr[0].equals("add")){
	            		int key = Integer.parseInt(arr[1]);
	            		String str = Integer.toString(key);
	            		if(!db.containsKey(key)){
	            			db.put(key,1);
	            		}
	            		else{
	            			db.put(key,db.get(key)+1);
	            		}
	            		System.out.println("ADD "+str);
	            		//System.out.println(db.get(key));
	            		out.println(db.get(key));
	            	}
	            	else if(arr[0].equals("read")){
	            		int key = Integer.parseInt(arr[1]);
	            		String str = Integer.toString(key);
	            		if(!db.containsKey(key)){
	            			outputLine = "READ "+str+" 0";
	            			System.out.println(outputLine);
	            			out.println(0);
	            		}
	            		else{
	            			String val = Integer.toString(db.get(key));
	            			outputLine = "READ "+str+" "+val;
	            			System.out.println(outputLine);
	            			out.println(db.get(key));
	            		}
	            	}
	            	else if(arr[0].equals("disconnect")){
	            		System.out.println("DIS");
	            		break;
	            	}
	            }
	        }//catch (InterruptedException e){ }
	         catch (IOException e) {
            	System.out.println("Exception caught when trying to listen on port "
                	+ "5000" + " or listening for a connection");
            	System.out.println(e.getMessage());
        	}
	    }
	}

	public static void main(String[] args){
		BasicServer serve = new BasicServer();
		//System.out.println("trying");
		serve.run();
	}
}