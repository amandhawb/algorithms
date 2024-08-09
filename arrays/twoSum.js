// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Input: nums = [3, 5, -4, 8, 11, 1, -1, 6], target = 8
// Output: [0,1]

// FORTH TIME
// 9 minutes - not looking, but insecure with the response
function twoSum(array, target) {
    let hashMap = new Map();
    for(let i = 0; i < array.length; i++) {
        let curr = array[i];
        if(!hashMap.has(target - curr)) {
            hashMap.set(curr, i);
        } else {
            let position = hashMap.get(target - curr);
            return [position, i];
        }
    }
    return false;
}

console.log(twoSum([3, 5, -4, 8, 11, 1, -1, 6], 8))


// THIRD TIME:
// 5 minutes - not looking
// time: O(n);
// space: O(n);

// function twoSum(array, target) {
//     let map = new Map();

//     for(let i = 0; i < array.length; i++) {
//         let currentElement = array[i];
//         if(map.has(target - currentElement)) {
//             let positionOfElement = map.get(target - currentElement);
//             return [positionOfElement, i];
//         } else {
//             map.set(currentElement, i);
//         }
//     }

//     return false;
// }

// console.log(twoSum([3, 5, -4, 8, 11, 1, -1, 6], 8));

// SECOND TIME: 15 min ("colando")
// complexity time: O(n)
// complexity space: O(n)
// function twoSum(array, target) {
//     let map = new Map();
//     for(let i = 0; i < array.length; i ++) {
//         let current = array[i];

//         if(map.has(target - current)) {
//             let position = map.get(target - current);
//             return [position, i]
//         } else {
//             map.set(current, i);
//         }
//     }
// }

// console.log(twoSum([3, 5, -4, 8, 11, 1, -1, 6], 10));


// time O(n)
// space O(n)
// function twoSum(array, target) {
//     let hashMap = new Map();
//     for(let i = 0; i < array.length; i ++) {
//         let currentElement = array[i];
//         if(hashMap.has(target - currentElement)) {
//             return [currentElement, i]
//         } else {
//             hashMap.set(currentElement, i);
//         }
//     }
// }