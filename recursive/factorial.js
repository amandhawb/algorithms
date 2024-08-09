// Given a number n return n!


// SECOND TIME:
// 5 minutes looking the solved function
// complexity time = O(1) --> wrong?
// complexity space = O(n) --> wrong?
function factorial(n) {
    console.log(n)
    if(n == 1) {
        return 1;
    }
    return n * factorial(n -1);
}


// 15 minutes
// Complexity time: O(n)
// Complexity space: O(1) 

// function factorial(n) {
//     if(n == 1) {
//         return 1;
//     }
//     let recursive = factorial(n - 1);
//     return n * recursive;
// }

console.log(factorial(4));