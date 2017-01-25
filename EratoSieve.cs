// Sieve of Eratosthenes
// January 21st, 2017

using System;
using System.Collections.Generic;

public class EratoSieve{
    public static void Main(string[] args){
        List<int> desired_primes = EratoPrimes.GeneratePrimes(100);
        foreach(int primenumber in desired_primes){
          Console.WriteLine(primenumber);
        }
  }
}

// traditional way (i.e., similar to Python)
public class EratoPrimes{
    public static List<int> GeneratePrimes(int limit){
        // set up indexed array of candidates:
        int[,] first_array = new int[limit,2];
        for(int i=0; i<limit; i++){
            first_array[i,0] = i;
            first_array[i,1] = 1;
        }
        first_array[0,1] = 0;
        first_array[1,1] = 0;
        // set up dynamic list of primes:
        List<int> primes = new List<int>();
        // begin Sieve:
        for(int a=2; a < limit; a++){
            if(first_array[a,1]==1){
                primes.Add(first_array[a,0]);
                for(int b = a*a; b < limit; b+=a){
                    first_array[b,1]=0;
                }
            }
        }
        return primes;
    }
}
