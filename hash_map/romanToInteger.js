// Given a roman numeral, convert it to an integer.
// Input: s = "III"
// Output: 3

function romanToInteger(roman) {
    const hash = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    let result = 0;

    for(let i = 0; i < roman.length; i++) {
        let curr = hash[roman[i]];
        let next = hash[roman[i +1]];

        if(curr < next) {
            result += next - curr;
            i++
        } else {
            result += curr;
        }
    }

    return result;
}

console.log(romanToInteger("IV"));