// Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.
// INPUT:
//        1
//     /      \
//    2         3
//   /   \    /   \
//  4     5   6     7
// /  \      /
// 8    9   10
// OUTPUT:
// [15, 16, 18, 10, 11]

class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
}


// space: O(n)
// time: O(n)
function brunchSum(root) {
    let sums = [];
    calculateBrunchSum(root, 0, sums);
    return sums;
}

function calculateBrunchSum(node, runningSum, sums) {
    if(node == null) {
        return
    }

    let newRunningSum = runningSum + node.value;

    if(node.left == null && node.right == null) {
        sums.push(newRunningSum);
        return
    }

    calculateBrunchSum(node.left, newRunningSum, sums);
    calculateBrunchSum(node.right, newRunningSum, sums);
}
