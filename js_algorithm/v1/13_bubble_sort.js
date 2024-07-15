// YouTube https://www.youtube.com/watch?v=gqMjdM8FsrE&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=20
// https://www.youtube.com/watch?v=xdCgW2a3r_Q&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=21

/*
 * Problem - Given a **stored** array of 'n' elements and a target element 't', find the index of 't', in the array. Return  -1 if the target element is not found,
 * Binary search only works on sorted array. If there is not sorted array to work with use linear search or sort the array and use binary search
 *
 * const arr = [-6, 20, 8, -2, 4]
 * bubbleSort(arr) => should return [-6, -2, 4, 8, 20]
 *
 * Compare adjacent elements in the array and swap the positions if they are not in the intended order
 * Repeat the instruction as you step through each element in the array
 * Once you step through the whole array with no swaps, the array is sorted
 *
 * Example
 * This is an example array [-6, 20, 8, -2, 4]
 * Do not swap first two elements -6 and 20 sonce  2nd item is greater than first One. Modified array [-6, 20, 8, -2, 4]
 * Swap next two elements 20 and 8 since next item is less than previous one ( 20 > 8). Modified array [-6, 8, 20, -2, 4]
 * Swap next two elements 20 and -2 since next item is less than previous one ( 20 > -2). Modified array [-6, 8, -2, 20, 4]
 * Swap next two elements 20 and 4 since next item is less than previous one ( 20 > -2). Modified array [-6, 8, -2, 20, 4]
 * End of array, elements swapped? yes? repeat the comparison.
 */


 function bubbleSort(arr){
   let swapped;
   do{
     swapped = false;
     for (var i = 0; i < arr.length - 1; i++) {
       if(arr[i] > arr[i+1]){
         let temp = arr[i];
         arr[i] = arr[i+1];
         arr[i+1] = temp;
         swapped = true;
       }
     }
   }while(swapped){

   }
 }


 const arr = [-6, 20, 8, -2, 4];

 bubbleSort(arr);
console.log(arr);
// Big-O = O(n^2)
