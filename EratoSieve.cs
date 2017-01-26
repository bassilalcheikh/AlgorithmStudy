// Sieve of Eratosthenes
// January 21st, 2017

using System;
using System.Collections.Generic;
using System.Diagnostics;

public class EratoSieve{
    public static void Main(string[] args){
        Stopwatch stopwatch = Stopwatch.StartNew();
        List<long> desired_primes = EratoPrimes.GeneratePrimes(10000);
        stopwatch.Stop();
        Console.WriteLine(stopwatch.ElapsedMilliseconds);
        /*foreach(int primenumber in desired_primes){
            Console.WriteLine(primenumber);
        }*/
  }
}

public class EratoPrimes{
    public static List<long> GeneratePrimes(long limit){
        long[,] first_array = new long[limit,2];
        for(long i=0; i<limit; i++){
            first_array[i,0] = i;
            first_array[i,1] = 1;
        }
        first_array[0,1] = 0;
        first_array[1,1] = 0;

        List<long> primes = new List<long>();

        for(long a=2; a < limit; a++){
            if(first_array[a,1]==1){
                primes.Add(first_array[a,0]);
                for(long b = a*a; b < limit; b+=a){
                    first_array[b,1]=0;
                }
            }
        }
        return primes;
    }
}
