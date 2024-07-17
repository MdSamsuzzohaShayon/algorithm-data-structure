// Tutorial - https://www.youtube.com/watch?v=x3rkUQcfFww&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=28

function cartesianProduct(arr1, arr2) {

    const result = [];

    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr2.length; j++) {
            result.push([arr1[i], arr2[j]]);
        }
    }

    return result;
}

const sArr1 = [1, 2],
    sArr2 = [3, 4, 5];

console.log(cartesianProduct(sArr1, sArr2)); // [ [1,3], [1,4], [1,5], [2, 3], [2,4], [2,5] ]
// Big-O = O(mn) because both array has different length