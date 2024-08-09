// Given an array such [1, 2, 3, 4, 10, 11, 0] find the bigger number.
// e.g: return 11

// SECOND TRY:
// 1:47, not looking the response
// space complexity: O(1)
// time complexity: O(n)
// function findMaxNumber(array) {
//     let currBigger = 0;
//     for(let i = 0; i < array.length; i++) {
//         if(array[i] > currBigger) {
//             currBigger = array[i];
//         }
//     }
//     return currBigger;
// }

// console.log(findMaxNumber([1, 2, 3, 4, 10, 0]));


// FIRST TRY 5 minutes
// Complexity time: O(n * log n)
// Complexity space: O(1)
function findMaxNumber(arr) {
    console.log("ENTERED ARRAY", arr);
    arr.sort((a,b) => a -b);
    console.log("SORTED", arr);
    return arr[arr.length-1];
}

console.log(findMaxNumber([11,10,1,2,3,4,0]));

// SECOND TRY 2 minutes
// Complexity time: O(n)
// Complexity space: O(1)
// function findMaxNumberII(arr) {
//     let currentBigger = 0;

//     for(let i = 0; i < arr.length; i++) {
//         if(arr[i] > currentBigger) {
//             currentBigger = arr[i];
//         }
//     }

//     return currentBigger;
// }