const text = "the quick fox jumps over the quick fox";

const nGrams = (text) => {
  let map = new Map();
  let splittedText = text.split(' ');

  for(let i = 0; i < splittedText.length; i++) {
    if(!map.has(splittedText[i])) {
        map.set(splittedText[i], 1);
    } else {
        let value = map.get(splittedText[i]);
        map.set(splittedText[i], value +1);
    }
  }
  return map;
}

console.log(nGrams(text));

//console.log(nGrams(text, 1))
// {
//   "the": 2,
//   "quick": 2,
//   "fox": 2,
//   "jumps": 1,
//   "over": 1,
// }



// in the future, increment the function:

//console.log(nGrams(text, 2))
// {
//   "the quick": 2,
//   "quick fox": 2,
//   "fox jumps": 1,
//   "jumps over": 1,
//   "over the": 1
// }

//console.log(nGrams(text, 3))
// {
//   "the quick fox": 2,
//   "quick fox jumps": 1,
//   "fox jumps over": 1,
//   "jumps over the": 1,
//   "over the quick": 1
// }

//function split(text, n) {
    //     let splittedText = text.split(' ');
    //     let response = [];
    //     // if(n <= 0 || n > splittedText.length) {
    //     //     return false;
    //     // } else if(n == splittedText.length) {
    //     //     return [text]
    //     // } else if(n == 1) {
    //     //     return splittedText;
    //     // }
        
    //     // ['The quick']
    
    //     for(let i = 0; i < splittedText.length; i =  i + 2) {
    //         response.push(splittedText[i] + ' ' + splittedText[i +1]);
    //     }
    
    //     return response;
        
    // }