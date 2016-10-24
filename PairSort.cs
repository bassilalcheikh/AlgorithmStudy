using System;
namespace Algorithms{

    public class PairSort{

        public int[] int_array {get; set;} //attributes method

        public PairSort(int[] Int_Array){ //accessor method
            int_array = Int_Array;
        }

        public int[] IntPairs(int[] int_array){
            //int length_parity = int_array.Length%2; (FEATURE TO BE LATER INCLUDED)

            if(int_array.Length%2 == 1){
    			do{
    				int_array[int_array.Length-1]=0;
    				int_array=SortLine(SortLine(int_array,0,int_array.Length-2),1,int_array.Length-3);
    			}while(int_array[int_array.Length-1] != 0);
    		}
    		else{
    			do{
    				int_array[int_array.Length-1]=0;
    				int_array=SortLine(SortLine(int_array,0,int_array.Length-3),1,int_array.Length-2);
    			}while(int_array[int_array.Length-1] != 0);
    		}
            return int_array;
        }

        private int[] SortLine(int[] input_array1, int entry_spot, int end_spot){
            int indicator = input_array1.Length-1;
            int length = end_spot - entry_spot +1;
            int[] output_array = new int[input_array1.Length];
            output_array[indicator] = input_array1[indicator]; //will never be compared, but must always transfer along
            output_array[indicator-1] = input_array1[indicator-1]; //may not always be compared; if they were, however, their new values would be appropriately substituted
            output_array[0] = input_array1[0];
                for(int i=entry_spot; i<(length/2+entry_spot); i++){
                    if (input_array1[2*i-entry_spot] <= input_array1[(2*i)+1-entry_spot]){
                        output_array[2*i-entry_spot] = input_array1[2*i-entry_spot];
                        output_array[(2*i)+1-entry_spot] = input_array1[(2*i)+1-entry_spot];
                    }
                    else {
                        output_array[2*i-entry_spot] = input_array1[(2*i)+1-entry_spot];
                        output_array[(2*i)+1-entry_spot] = input_array1[2*i-entry_spot];
                        output_array[indicator]++;
                    }
                }
            return output_array;
        }
    }
}
