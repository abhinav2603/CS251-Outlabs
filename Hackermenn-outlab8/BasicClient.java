import java.net.*;
import java.io.*;
import java.util.*;

public class BasicClient extends Thread{
	static File file;

	String input;
	public void run(){

		try{
			BufferedReader br = new BufferedReader(new FileReader(file));
			int global = 0,delta;
			Map<Integer,Integer> db = new HashMap<Integer,Integer>();
			boolean print_state = false;

			while((input = br.readLine()) != null){

				String[] arg = input.split(" ");
				 //System.out.println(arg[0]);
				// System.out.println(arg[1]);
				if(arg[0].equals("sleep")){
					//System.out.println("rand");

					try{	
						Thread.sleep(Integer.parseInt(arg[1]));
						//System.out.println("slept for this much time");
					}catch (InterruptedException e){ }
				}
				else if(arg[0].equals("connect")){
					//System.out.println("rand");
					String hostName = arg[1];
	        		int portNumber = Integer.parseInt(arg[2]);
	        		//System.out.println("connecting to host");
	        		try(
	        			Socket socket = new Socket(hostName, portNumber);
	            		PrintWriter out = new PrintWriter(socket.getOutputStream(),true);
	            		BufferedReader in = new BufferedReader(
	                	new InputStreamReader(socket.getInputStream()));
	        		) {
	        			System.out.println("OK");
	        			print_state = true;
	        			String fromServer,fromUser,cmd;
	        			String[] arr;
	        			//System.out.println(cmd);
	            		while(true){
	            			if((cmd = br.readLine()) != null){;
		            			arr = cmd.split(" ");
		            			if(arr[0].equals("add")){
		            				out.println(cmd);
		            				fromServer = in.readLine();
		            				//System.out.println(fromServer);
		            				int key = Integer.parseInt(arr[1]),val = Integer.parseInt(fromServer);
		            				db.put(key,val);
		            				//System.out.println(db.get(key));
		            			}
		            			else if(arr[0].equals("read")){
		            				out.println(cmd);
		            				fromServer = in.readLine();
		            				//System.out.println(fromServer);
		            				int key = Integer.parseInt(arr[1]),val = Integer.parseInt(fromServer);
		            				if(db.containsKey(key)){
		            					delta = val - db.get(key);
		            				}
		            				else{
		            					delta = val;
		            				}
		            				global = global + delta;
		            				//System.out.print(fromServer);
		            				System.out.print(fromServer+" "+Integer.toString(delta)+'\n');
		            			}
		            			else if(arr[0].equals("disconnect")){
		            				out.println(cmd);
		            				System.out.println("OK");
		            				break;
		            			}
	            			}
	            		}
	        		}catch(Exception e) {
	           			System.err.println("No Server");
	           			//print_state = false;
	           		}
	          //  		catch (IOException e) {
			        //     System.err.println("Couldn't get I/O for the connection to " +
			        //         hostName);
			        //     System.exit(1);
			        // }
				}
			}
			if(print_state){
				System.out.println(global);
			}
		}
		catch (IOException e) {
            System.err.println("Couldn't get I/O for the file");
            System.exit(1);
        }
	}

	public static void main(String[] args){
		file = new File(args[0]);
		BasicClient client = new BasicClient();
		// System.out.println("connecting: 5000");
		client.run();
	}
}