// Tutorial - https://www.youtube.com/watch?v=gqMjdM8FsrE&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=20
function bubbleSort(arr) {
    let swapped = false;
    do {
        swapped = false;
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                const temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapped = true;
            }
        }
    } while (swapped)

}

const arr = [8, 20, -2, 4, -6];
bubbleSort(arr);
console.log(arr);
// Big-O = O(n^2) Quadratic time complexity