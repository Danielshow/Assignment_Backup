/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package SnakeEyeCount;

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
        int die1, die2, rolls;
        
        rolls = 0;
        while (true){
          die1 = (int)(Math.random() * 6) + 1;
          die2 = (int)(Math.random() * 6) + 1;
          rolls += 1;
          if (die1 == 1 && die2 == 1){
            break;
          }
        }
        
        TextIO.putln("Snake Eyes after " + rolls + " rolls of the dice");
    }
    
}
