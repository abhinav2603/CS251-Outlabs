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
import java.sql.Connection;
import java.sql.Statement;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.io.*;

public class FetchAndProcessFromNetwork implements FetchAndProcess {
    private Map<String, String> data;

    @Override
    public Map<String, String> exposeData() {
	return data;
    }

    @Override
    public void fetch(List<String> paths){
	// Implement here
        int len=paths.size();
        data=new HashMap<String, String>();
        for(int i=0;i<len;i++){
            try{
                URL url=new URL(paths.get(i));
                URLConnection url_connect = url.openConnection();
                BufferedReader file = new BufferedReader(new InputStreamReader(url_connect.getInputStream()));
                String str=file.readLine();
                while(str!=null){
                    if(data.containsKey(str)==false){
                        data.put(str,paths.get(i));
                    }
                    else if(data.get(str).contains(paths.get(i))){
                        continue;
                    }
                    else{
                        data.put(str,data.get(str)+";"+paths.get(i));
                    }
                    str=file.readLine();
                }
                file.close();
            }
            catch(MalformedURLException e){
                System.err.println(e.getMessage());
                continue;
            }
            catch(IOException e){
                System.err.println(e.getMessage());
                continue;
            }
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
