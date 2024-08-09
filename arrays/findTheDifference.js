// Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

// answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
// answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
// Note that the integers in the lists may be returned in any order.

// Input: nums1 = [1,2,3], nums2 = [2,4,6]
// Output: [[1,3],[4,6]]

// SECOND TIME:
// 5 minutes --> used map instead of set, which generated an error;
// complexity time: O(n)
// complexity space: O(n)
function findTheDifference(array1, array2) {
    let set1 = new Set(array1);
    let set2 = new Set(array2);

    let response1 = [];
    for(let i = 0; i < array1.length; i++) {
        if(!set2.has(array1[i])) {
            response1.push(array1[i]);
        }
    }

    let response2 = [];
    for(let i = 0; i < array2.length; i++) {
        if(!set1.has(array2[i])) {
            response2.push(array2[i]);
        }
    }

    return [response1, response2];
}

console.log(findTheDifference([1,2,3], [2,4,6]));












// time: O(n)
// space: O(n)
// 10 minutes
// function findTheDifference(nums1, nums2) {
//     let set1 = new Set(nums1);
//     let set2 = new Set(nums2);

//     let response1 = [];
//     for(const item of set1) {
//         if(!set2.has(item)) {
//             response1.push(item)
//         }
//     }

//     let response2 = [];
//     for(const item of set2) {
//         if(!set1.has(item)) {
//             response2.push(item);
//         }
//     }

//     return [response1, response2];
// }

// console.log(findTheDifference([1,3,3], [1,2,2]));