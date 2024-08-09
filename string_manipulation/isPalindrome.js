// Given an string s, determine if it is palindroome or not.
// example: arara --> true;

// THIRD TIME:
// 3:23 not looking response
// complexity time: O(n);
// complexity space: O(1);
function isPalindrome(string) {
    let rightPointer = string.length -1;
    let leftPointer = 0;

    for(let i = 0; i < string.length; i++) {
        if(string[rightPointer] !== string[leftPointer]) {
            return false
        } else {
            rightPointer = rightPointer -1;
            leftPointer = leftPointer +1;
        }
    }
    return true;
}

console.log(isPalindrome('ararae'));



// function isPalindrome(word) {
//     let left = 0;
//     let right = word.length -1;

//     while(left < right) {
//         if(word[left] != word[right]) {
//             return false
//         } else {
//             left++;
//             right--;
//         }
//     }
//     return true;
// }


// function isPalindromeNewArray(word) {
//     let newArray = [];

//     for(let i = word.length -1; i >= 0; i--) {
//         console.log(word[i]);
//         newArray.push(word[i]);
//     }

//     return word == newArray.join('');
// }

// console.log(isPalindromeNewArray('arara'));



// SECOND TIME:
// 3 minutes
// time Complexity: O(n)
// space complexity: O(1)
// function isPalindrome(word) {
//     let right = word.length -1;
//     let left = 0;

//     while(left <= right) {
//         if(word[left] != word[right]) {
//             return false
//         } else {
//             left += 1;
//             right -= 1;
//         }
//     }
//     return true;
// }

// console.log(isPalindrome('a'));


// using pointers:

// Space complexity: O(1)
// Time complexity: O(n)
// function isPalindromePointers(string) {
//     let right = string.length - 1;
//     let left = 0
  
//     while (left < right) {
//       if(string[right] != string[left]) {
//         return false
//       } else {
//         left += 1;
//         right -= 1;
//       }
//     }
  
//     return true;
// }

// // Space complexity: O(n)
// // Time complexity: O(n)
// function isPalindrome(string) {
//     let newString = [];
  
//     for(let i = string.length -1; i >= 0; i --) {
//       newString.push(string[i]);
//     }
  
//     return string == newString.join('');
//   }