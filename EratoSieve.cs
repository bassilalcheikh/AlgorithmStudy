// Sieve of Eratosthenes
// January 21st, 2017

using System;
using System.Collections.Generic;

public class EratoSieve{
    public static void Main(string[] args)
    {
        int[][] desired_primes = EratoPrimes.GeneratePrimes(10);
        Console.WriteLine("Hello.");

    }
}

// traditional way (i.e., similar to Python)
public class EratoPrimes{
    public static bool[] GeneratePrimes(int limit)
    {
        int[][] first_array = new int[limit][limit];
        //first_array[][0]=1;
        //first_array[][1]=1;
        for(int i=0; i<limit; i++){
            first_array[i][]=i;
        }

        for(int t=0; t<limit; t++){
            Console.WriteLine(first_array[t]);
        }
        return first_array;
    }
}
