import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.concurrent.*; 
import java.sql.Connection;
import java.sql.Statement;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.io.*;
/* add some more imports */

public class FetchAndProcessFromNetworkFast implements FetchAndProcess {
    private Map<String, String> data;

    @Override
    public Map<String, String> exposeData() {
	return data;
    }

    @Override
    public void fetch(List<String> paths) {	
	// Implement here, just do it parallely!
        class Fast implements Runnable{
            private String path;

            public Fast(String str){
                path=str;
            }

            public void run(){
                try{
                    URL url=new URL(path);
                    URLConnection url_connect = url.openConnection();
                    BufferedReader file = new BufferedReader(new InputStreamReader(url_connect.getInputStream()));
                    String str=file.readLine();
                    while(str!=null){
                        synchronized(data){
                            if(data.containsKey(str)==false){
                                data.put(str,path);
                            }
                            else if(data.get(str).contains(path)){
                                continue;
                            }
                            else{
                                data.put(str,data.get(str)+";"+path);
                            }
                        }
                        str=file.readLine();
                    }
                    file.close();
                }
                catch(MalformedURLException e){
                    System.err.println(e.getMessage());
                }
                catch(IOException e){
                    System.err.println(e.getMessage());
                }
            }
        }

        int len=paths.size();
        data=new HashMap<String, String>();
        
        ExecutorService threadPool=Executors.newFixedThreadPool(10);

        for(int i=0;i<len;i++){
            threadPool.execute(new Fast(paths.get(i)));
        }

        threadPool.shutdown();
        try{
            threadPool.awaitTermination(120, TimeUnit.SECONDS);
        }
        catch(InterruptedException e){
            System.err.println(e.getMessage());
        }
        return;
    }

    @Override
    public List<String> process() {
	// Implement here
	// Can you make use of the default implementation here?
	// See https://dzone.com/articles/interface-default-methods-java
        List<String> name=FetchAndProcess.super.process();
        try
        {
            FetchAndProcess.super.process();
            String dName = "org.sqlite.JDBC";
            Class.forName(dName);
            String tempDb = "pokemon.db";
            String db = "jdbc:sqlite";
            String dbUrl = db + ":" + tempDb;
            Connection conn = DriverManager.getConnection(dbUrl);
            Statement stmt=conn.createStatement();
            ResultSet rs=stmt.executeQuery("SELECT pokemon_name FROM (SELECT pokemon_name,COUNT(source_path) AS c FROM pokemon GROUP BY pokemon_name) WHERE c>1;");
            try 
            {
                while(rs.next())
                {
                    String sResult = rs.getString("pokemon_name");
                    System.out.println(sResult);
                }
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
            finally 
            {
                try { rs.close(); } 
                catch (Exception ignore) {}
            }
        }
        catch(Exception e){
            System.out.println(e);
        }
        return null;
    }
}
