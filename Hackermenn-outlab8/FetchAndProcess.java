import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.DriverManager;
import java.sql.ResultSet;

public interface FetchAndProcess {
    static String DB_NAME = "pokemon.db";
    static String TABLE_NAME = "pokemon";

    /* The map populated by fetch */
    // public Map<String, String> data = new HashMap<String, String>();
    
    // no default implementation
    void fetch(List<String> paths);

    // no default implementation
    Map<String, String> exposeData();
    
    /* Provides a default implementation that does a lot of work:
     * 1. Create the `TABLE_NAME` table if it does not exist (along with a uniqueness constraint).
     * 2. Inserts data into the table, safely. ensuring no duplication.
     * 3. Returns the Connection (useful for the FetchAndProcessNetwork* classes)
     */
    default List<String> process() {
        String sDriverName = "org.sqlite.JDBC";
        List<String> ret=new ArrayList<String>();
        String sDbUrl="";
        //int ins=0;
        try{
            Class.forName(sDriverName);
 
        // now we set up a set of fairly basic string variables to use in the body of the code proper
        String sJdbc = "jdbc:sqlite";
        sDbUrl = sJdbc + ":" + DB_NAME;
        // which will produce a legitimate Url for SqlLite JDBC :
        // jdbc:sqlite:hello.db
        int iTimeout = 30;
 
        // create a database connection
        Connection conn = DriverManager.getConnection(sDbUrl);
        conn.setAutoCommit(false);
        try {
            Statement stmt = conn.createStatement();
            try {
                stmt.setQueryTimeout(iTimeout);
                stmt.executeUpdate("CREATE TABLE IF NOT EXISTS "+TABLE_NAME+"(pokemon_name TEXT, source_path TEXT, UNIQUE(pokemon_name,source_path));");
                //System.out.println("table made");
                Map<String,String> dat=exposeData();
                for(String poke_name:dat.keySet())
                {
                    //System.out.println("Working with pokemon "+poke_name);
                    //System.out.println("Locations: "+dat.get(poke_name));
                    String[] locs=dat.get(poke_name).split(";",0);
                    for(String loc_name:locs)
                    {
                        //System.out.println("Location: "+loc_name);
                        try
                        {
                            stmt.executeUpdate("INSERT INTO "+TABLE_NAME+" VALUES(\""+poke_name+"\", \""+loc_name+"\");");
                            //System.out.println("Done this");
                            //ins++;
                        }
                        catch(Exception e)
                        {
                            //System.out.println(e);
                        }
                    }
                    
                }
                //ResultSet rs = stmt.executeQuery(sMakeSelect);
                
            } finally {
                try { stmt.close(); } catch (Exception ignore) {}
            }
        } finally {
            try {   conn.commit();
                    conn.close(); } catch (Exception ignore) {}
        }
        //System.out.println(ins);
        }
        catch(Exception e){
            ret.add(sDbUrl); 
            return ret;
        }
        return null;
	// you can use exposeData() here.
    }
}
