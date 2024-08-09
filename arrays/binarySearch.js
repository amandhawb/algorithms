// Write a function that takes in a sorted array of integers as well as a target integer and return the target. 
// [0, 1, 2, 3, 7, 60] 1

// array = [1,2]
// array[1] == 2
// array[array.length -1]

// THIRD TIME:
// 2 minutes
// complexity time: O(log n)
// complexity space: O(1)
function binarySearch(array, target) {
    let right = array.length -1;
    let left = 0;

    while (left <= right) {
        let middle = Math.floor((right + left) / 2);

        if(target > array[middle]) {
            left = middle + 1;
        } else if(target < array[middle]) {
            right = middle -1;
        } else if(target == array[middle]){
            return true
        }
    } 
    return false;
}




// SECOND TIME:
// 13 minutes looking up the working response
function binarySearch(array, target) {
    let right = array.length - 1;
    let left = 0;

    while(left <= right) {
        let middle = Math.floor((left + right) / 2);
        if(target > array[middle]) {
            left = middle + 1
        } else if(target < array[middle]) {
            right = middle - 1
        } else if(target == array[middle]) {
            return middle
        }
    }
}


// FIRST TIME:
// 40 minutes
// Complexity time: O(log n)
// Complexity space: O(1)
// function binarySearch(arr, target) {
//     let right = arr.length - 1;
//     let left = 0;

//     while(left <= right) {
//         let middle = Math.floor((right + left) / 2);
//         if(target > arr[middle]) {
//             left = middle + 1;
//         } else if(target < arr[middle]) {
//             right = middle - 1;
//         } else if(target == arr[middle]) {
//             return middle;
//         }
//     }

//     return -1;
// }

console.log(binarySearch([0, 1, 2, 3, 7, 60], 1));
