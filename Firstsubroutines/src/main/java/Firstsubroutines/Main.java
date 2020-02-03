/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package Firstsubroutines;
import java.util.Scanner;

/**
 *
 * @author danielshotonwa
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
      String reversed;
      String stripped;
      
      TextIO.putln("****************************************");
      TextIO.putln("Palindrome Check");

      TextIO.putln("Enter word to check for palindrome:");
      
      String word = TextIO.getln();
      stripped = removeNonAlphabets(word.toLowerCase());
      reversed = reverse(stripped);
      TextIO.putln("stripped: " + stripped);
      TextIO.putln("reversed: " + reversed);

      if (stripped.equals(reversed)){
        TextIO.putln("This IS a palindrome.");
      } else {
        TextIO.putln("This is NOT a palindrome.");
      }
    }

    /**
     * @desc - This function returns a reverse string
     * @param word - the string to reverse
     * @return String 
     */
    public static String reverse(String word) {
       String reverse;
       reverse = "";

       for (int i = word.length() - 1; i >= 0; i--) {
         reverse = reverse + word.charAt(i);
       }
       return(reverse);
    }

    /**
     * @desc - This function removes non alphabets from a string
     * @param word - A new string with all non alphabets stripped
     * @return String 
     */
    public static String removeNonAlphabets(String word){
      String new_string;
      new_string = "";      
      for (int i = 0; i < word.length(); i++){
        if (word.charAt(i) >= 'a' && word.charAt(i) <= 'z'){
          new_string += word.charAt(i);
        }
      }
      return new_string; 
    }

}
