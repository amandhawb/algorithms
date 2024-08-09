// You are given a non-negative integer array nums. In one operation, you must:

// Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
// Subtract x from every positive element in nums.
// Return the minimum number of operations to make every element in nums equal to 0.

// Example:
// Input: nums = [1,5,0,3,5]
// Output: 3
// Explanation:
// In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
// In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
// In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

function hasOnlyZeros(array) {
    for(let i = 0; i < array.length; i++) {
        if(array[i] > 0) {
            return false;
        }
    }
    return true;
}

function getSmallestNumber(array) {
    let smallest = Math.pow(10, 1000)
    for(let i = 0; i < array.length; i++) {
        if(array[i] < smallest && array[i] != 0) {
            smallest = array[i];
        }
    }
    return smallest;
}

function minimumOperations(nums) {
    let rounds = 0;
    while(hasOnlyZeros(nums) == false) {
        rounds++;
        let smallestNumber = getSmallestNumber(nums);

        for(let i = 0; i < nums.length; i++) {
            if(nums[i] > 0) {
                nums[i] = nums[i] - smallestNumber;
            }
        }
    }
    return rounds;
}

console.log(minimumOperations([0]));