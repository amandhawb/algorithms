// Given an array of letters (['a', 'b', 'a', 'c', 'b', 'a', 'e']) return the number of occurances for duplicated letters. 
// Example of return: [['a', 3], ['b', 2]]

function countDuplicatedLetter(arr) {
    let mapOfLetters = new Map();

    for(let i = 0; i < arr.length; i++) {
        let currentElement = arr[i];
        if(!mapOfLetters.has(currentElement)) {
            mapOfLetters.set(currentElement, 1);
        } else {
            let existedElement = mapOfLetters.get(currentElement);
            mapOfLetters.set(currentElement, existedElement + 1);
        }
    }

    let result = [];

    mapOfLetters.forEach((value, key) => {
        if(value > 1) {
            result.push([key, value]);
        }
   
    });

    return result;
}

console.log(countDuplicatedLetter(['a', 'b', 'a', 'c', 'b', 'a', 'e']));