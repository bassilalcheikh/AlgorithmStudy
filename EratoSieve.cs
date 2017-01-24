// Sieve of Eratosthenes
// January 21st, 2017

using System;
using System.Collections.Generic;

public class EratoSieve{
    public static void Main(string[] args)
    {
        bool[] desired_primes = EratoPrimes.GeneratePrimes(10);
        Console.WriteLine("Hello.");

    }
}

// traditional way (i.e., similar to Python)
public class EratoPrimes{
    public static bool[] GeneratePrimes(int limit)
    {
        string test_return = "stuff";
        //int[,] first_array = new int[limit];
        bool[] arr_1 = new bool[limit];
        arr_1[0]=true;
        arr_1[1]=true;
        enum enum_arr{arr_1};

        for(int t=0; t<limit; t++){
            Console.WriteLine(arr_1[t]);

        }
        return arr_1;
    }
}
