// Tutorial - https://www.youtube.com/watch?v=lWLTHsQnHDI&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=25


function quickSort(arr) {
    if(arr.length < 2) return arr;

    const pivort = arr[arr.length - 1];
    const left = [],
        right = [];

    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] < pivort) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    return [...quickSort(left), pivort, ...quickSort(right)];
}




const sArr = [8, 20, -2, 4, -6];
console.log(quickSort(sArr));

// Big-O worst case - O(n^2)
// Big-O Average case - O(n log n)

