// Given an array such [1, 2, 3, 4, 10, 11] find the lowest number.
// e.g: return 1

// 5 minutes
// Complexity time: O(n)
// Complexity space: 0(1)

function findMinNumber(arr) {
    let currentLowest = Number.MAX_SAFE_INTEGER;

    for(let i = 0; i < arr.length; i++) {
        if(arr[i] < currentLowest) {
            currentLowest = arr[i];
        }
    }

    return currentLowest;
}

