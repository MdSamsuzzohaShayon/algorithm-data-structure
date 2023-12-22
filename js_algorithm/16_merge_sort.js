/*
 * YouTube - https://www.youtube.com/watch?v=qInXNtKaf4Q&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=26
 *
 * Divide the array into sub arrays, each containing only one element (An array with one element is considered sorted)
 * Repeatedly merge the sub arrays to product new sorted sub arrays until there is only one sub array remaining. That will be the sorted array.
 *
 */


/*
 * Since it contains loop it is linear time complexity
 * Big-O = O(n)
 */
 function merge(leftArr, rightArr){
   const sortedArr = [];
   while (leftArr.length && rightArr.length) {
     if(leftArr[0] <= rightArr[0]){
       sortedArr.push(leftArr.shift());
     }else{
       sortedArr.push(rightArr.shift());
     }
   }

   return [...sortedArr, ...leftArr, ...rightArr];
 }


/*
 * Recursivly devides probelm into half
 * Big-O = O(log n)
 */
 function mergeSort(arr){
   if(arr.length < 2) return arr;
   const mid = Math.floor(arr.length / 2);
   const leftArr = arr.slice(0, mid);
   const rightArr = arr.slice(mid);
   return merge(mergeSort(leftArr), mergeSort(rightArr));
 }


 const arr = [8, 20, -2, 4, -6];
 console.log(mergeSort(arr)); // Expected return: [-6,-2,4,8,20]

/*
 * Conbine 2 function 'merge' Big-O = O(n) and 'mergeSort' Big-O = O(log n) for the time complexity 
 * Big-O = O(n log n)
 */
