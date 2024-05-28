// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:
// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

// Example 1:
// Input: s = "()"
// Output: true

// Example 2:
// Input: s = "(]"
// Output: false

// SECOND TIME
// 6 minutes
// time complexity: O(n)
// space complexity: O(n)
function validParentheses(string) {
    let stack = [];

    for(let i = 0; i < string.length; i++) {
        let curr = string[i];
        if(curr === '(' || curr === '{' || curr === '[') {
            stack.push(curr);
        } else {
            if(stack.length === 0) {
                return false // the first element is closing brackets
            }

            let lastBracket = stack.pop();
            if((curr === ')' && lastBracket !== '(') ||
                (curr === '}' && lastBracket !== '{') ||
                (curr === ']' && lastBracket !== '[')) {
                return false;
            }
        }
    }

    return stack.length === 0;
}

console.log(validParentheses('[[[[[[['));


















// time complexity: O(n)
// space complexity: O(n) --> in the worst case, all the elements could be open brackets, and they will be added on the stack.
// function validParentheses(string) {
//     let stack = [];

//     for(let i = 0; i < string.length; i++) {
//         let curr = string[i];

//         if(curr == '(' || curr == '{' || curr == '[') {
//             stack.push(curr);
//         } else {
//             if(stack.length == 0) {
//                 return false // it means the first element on string is a closing bracket
//             }
//             let lastBracket = stack.pop();

//             if(
//                 (curr == ')' && lastBracket !== '(') || 
//                 (curr == '}' && lastBracket !== '{') ||
//                 (curr == ']' && lastBracket !== '[')) {
//                 return false;
//             }
//         }
//     }
//     return stack.length == 0;
// }

// console.log(validParentheses('[}'));