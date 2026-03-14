import java.util.Scanner;
public class TaskOne{

    public static void main(String...args){
    
    Scanner input = new Scanner(System.in);
    int sumOfAllSquares = 0;

    int sumOfOddSquares = 0;    
    
    int sumOfEvenSquares = 0;

    int mean = 1;

    int squaresOfOdd = 0;

    int squaresOfEven = 0;

    int sumOfAllNumber = 0;

    int sumOfEven = 0;

    int sumOfOdd = 0;

    for(int count = 1 ;count <= 10;count++){

    System.out.println("Enter number "+(count )+" :");

   int  userInput = input.nextInt();

    sumOfAllNumber += userInput;
    mean = sumOfAllNumber / userInput;
 

        if(userInput % 2 == 0){
        sumOfEven += userInput;
        squaresOfEven = userInput * userInput;
        sumOfEvenSquares += squaresOfEven;
 
        System.out.println(" Square of even number is "+squaresOfEven);
 
    }    else{
         sumOfOdd += userInput;
        squaresOfOdd = userInput * userInput;
         sumOfOddSquares += squaresOfOdd;
        System.out.println(" Square of even number is "+squaresOfOdd);
    
      }
 sumOfAllSquares = sumOfEvenSquares + sumOfOddSquares;

    }

               
    System.out.println(" Sum of odd numbers "+sumOfOdd);

     System.out.println(" Sum of Even numbers "+ sumOfEven);

       System.out.println(" Sum of all numbers "+sumOfAllNumber);

        System.out.println("The mean   number is "+mean);

            System.out.println(" The sum of Squares of even number is "+sumOfEvenSquares);

            System.out.println(" The sum of Squares of odd number is "+sumOfOddSquares);
            System.out.println(" The sum of all Squares is "+sumOfAllSquares);
 
    }
}


























