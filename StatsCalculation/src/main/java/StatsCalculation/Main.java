/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package StatsCalculation;

/**
 *
 * @author danielshotonwa
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // create an array of the given numbers
        int[] numbers = new int[]{5, 7, 12, 23, 3, 2, 8, 14, 10, 5, 9, 13};
        StatCalc myStatCalc;
        myStatCalc = new StatCalc();
        for (int i=0; i < numbers.length; i++){
          // enter the array to StatCalc class
          myStatCalc.enter(numbers[i]);
        }
        // print the needed result
        System.out.println("Count: " + myStatCalc.getCount());
        System.out.println("Mean: " + myStatCalc.getMean());
        System.out.println("Standard Deviation: " + myStatCalc.getStandardDeviation());
    }

}
