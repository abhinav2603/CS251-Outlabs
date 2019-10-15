import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Path; 
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.io.*;

public class FetchAndProcessFromDisk implements FetchAndProcess {
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
	    		Path path = Paths.get(paths.get(i));
	    		Path fileNameWithExtension = path.getFileName();
	    		String s=fileNameWithExtension.toString();
	    		String fileName=s;
	    		if(s.contains(".")){
	    			int index=s.lastIndexOf(".");
	    			fileName=s.substring(0,index);
				}
				FileInputStream file=new FileInputStream(paths.get(i));
	    		int temp=file.read();
				while(temp!=-1){
					String str="";
					while((char)temp!='\n'){
						str+=(char)temp;
						temp=file.read();	
					}
					if(data.containsKey(str)==false){
						data.put(str,fileName);
					}
					else if(data.get(str).contains(fileName)){
						continue;
					}
					else{
						data.put(str,data.get(str)+";"+fileName);
					}
					temp=file.read();
				}
				file.close();
	  	  	}
		  	catch(FileNotFoundException e){
		  		System.err.println(e.getMessage());
		  		continue;
		  	}
		  	catch(NullPointerException e){
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
}
