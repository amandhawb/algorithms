// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

// FIRST SOLUTION:
// Space: O(m) where m is the quantity of unique values in the array because the number of unique elements in the array will be size of the hash map.
// Time: O(n) where n is the array size because I need to traverse all the array once.

function majorityElement(nums) {
    let hashTable = new Map();

    for(let i = 0; i < nums.length; i++) {
        if(!hashTable.has(nums[i])) {
            hashTable.set(nums[i], 1);
        } else {
            let quantity = hashTable.get(nums[i]);
            hashTable.set(nums[i], quantity + 1);
        }
    }

    let maxKey = null;
    let maxQuantity = 0;

    for(let [key, value] of hashTable.entries()) {
        if(value > maxQuantity) {
            maxKey = key;
            maxQuantity = value;
        }
    }

    return maxKey;

}

console.log(majorityElement([3,2,3]));
console.log(majorityElement([2,2,1,1,1,2,2]));