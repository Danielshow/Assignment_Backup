package ExceptionsAssignment;

import java.io.*;
import java.net.*;

public class Exceptions {
  public static void main (String[] args) {
	  InputStream input = null;
	  OutputStream output = null;
	  
	  TextIO.put("Enter a URL to read: ");
	  String fileUrl = TextIO.getln();
	  TextIO.putln("Enter the filename: ");
	  String fileName = TextIO.getln();
	  try {
		  URL url = new URL(fileUrl);
		  try {
		      input = url.openStream();
		      try {
		        output = new FileOutputStream(fileName);
		        try {
		          copyStream(input, output);
		        } catch(IOException e) {
		        	TextIO.putln("Cannot Write to file");
		        } finally {
		        	 input.close();
		   		  	 output.close();
		   		  	 TextIO.putln("Done writing to file");
		        }
		      } catch(FileNotFoundException e) {
		    	  TextIO.putln("File cannot be opened or cannot be created");
		      }
		  } catch(IOException e) {
			  TextIO.putln("Web address is not found");
		  }
		  
	  } catch(MalformedURLException e) {
		  TextIO.putln("This is a malform URL");
	  }
  }
  
  private static void copyStream(InputStream in, OutputStream out)
  throws IOException {
	  int oneByte = in.read();
	  while (oneByte >= 0) { // negative value indicates end-of-stream
		  out.write(oneByte);
		  oneByte = in.read();
	  }
   }
}
