// Tutorial - https://www.youtube.com/watch?v=Wu_mDUIsTVE&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=22

 function insertionSort(arr){
    for (let i = 0; i < arr.length; i++) {
      const numToInsert = arr[i];
      let j = i - 1;
      while ( j >= 0 && arr[j] > numToInsert) {
        arr[j+1] = arr[j];
        j = j-1;
      }   
      arr[j+1]      = numToInsert
    }
 }

 const arr = [8, 20, -2, 4, -6];
 insertionSort(arr);
 console.log(arr);

 // Big-O = O(n^2) Quadratic time complexity