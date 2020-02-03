/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package NumbeOfCone;

/**
 *
 * @author danielshotonwa
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int count = 0;
        int strawcount = 0;
        try {
           TextIO.readFile("icecream.dat");
        }catch(IllegalArgumentException e){
          TextIO.put(e);
        }
        
        
        while(!TextIO.eof()){
            count += 1;
            if (TextIO.getln().equals("Strawberry")){
                strawcount += 1;
            }
        }
        
        TextIO.putln("The number of Icecream in the file is " + String.valueOf(count));
        TextIO.putln("The number of StrawBerry in the file is " + String.valueOf(strawcount));
    }
    
}
