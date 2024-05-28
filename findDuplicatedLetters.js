// Given an array [a, b, c, b, f] find if there is a duplicated element. Return the duplicated element
// result = b
// assuming there will always be one and maximum one element duplicated

// THIRD TIME
// 2 minutes, not looking the response
function findDuplicatedLetters(array) {
    let set = new Set();

    for(let i = 0; i < array.length; i++) {
        if(set.has(array[i])) {
            return array[i];
        } else {
            set.add(array[i]);
        }
    }
    return false;
}

console.log(findDuplicatedLetters(['a', 'b', 'c', 'b', 'f']));

// SECOND TRY:
// 4 minutes
// time complexity: O(n)
// space complexity: O(n)
// function findDuplicatedLetters(array) {
//     let set = new Set();

//     for(let i = 0; i < array.length; i++) {
//         if(!set.has(array[i])) {
//             set.add(array[i])
//         } else {
//             return array[i]
//         }
//     }

//     return false;
// }

// console.log(findDuplicatedLetters(['a', 'b', 'c', 'f']));

// 10 minutes
// Complexity time: O(n)
// Complexity space: O(n)
// function findDuplicatedLetters(arr) {
//     let setCounter = new Set();

//     for(let i = 0; i < arr.length; i++) {
//         if(setCounter.has(arr[i])) {
//             return arr[i];
//         } else {
//             setCounter.add(arr[i]);
//         }
//     }
// }

// console.log(findDuplicatedLetters(['a', 'b', 'c', 'b', 'f']));

// Resolve the same algorithm without using map or set
// 10 minutes
// Complexity time: O(nˆ2)
// Complexity space: O(1)
// function findDuplicatedLettersUsingFor(arr) {
//     for(let i = 0; i < arr.length; i++) {
//         for(let j = i + 1; j < arr.length; j++) {
//             if(arr[i] == arr[j]) {
//                 return arr[i];
//             }
//         }
//     }
// }

// console.log(findDuplicatedLettersUsingFor(['a', 'b', 'c', 'd', 'f']));
