// Given an array with n elements, and a target t, traverse the array and return a index of the target.
// e.g. [1, 2, 3, 5, 6, 7] t = 7, return 5

// FIRST TRY
// 1 minute and 30 seconds
// time: O(n)
// space: O(1)
function naiveSearch(array, target) {
    for(let i = 0; i < array.length; i++) {
        if(array[i] == target) {
            return i;
        }
    }
    return false;
}

console.log(naiveSearch([1, 2, 3, 5, 6], 1));