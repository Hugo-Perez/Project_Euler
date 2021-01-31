package main;

import java.math.BigInteger;

public class Main20 {
  // Find the sum of the digits in the number 100!
  public static void main(String[] args) {
    // 100 Factorial calculation
    BigInteger factorial = new BigInteger("100"); 
    for (int i = 100; i > 1; i--) {
      factorial = factorial.multiply(new BigInteger(String.valueOf(i)));
    }

    // Convert value to char array
    char[] digits = factorial.toString().toCharArray();

    //Output digit sum
    int result = 0;
    for (char digit: digits) {
      result += Character.getNumericValue(digit);
    }
    System.out.println("Result: " + result);
  }
}
