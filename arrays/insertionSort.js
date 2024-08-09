// Write a function that takes in an array of integers and returns a sorted version of that array. 
// Use the Insertion Sort algortihm to sort the array. 

// input [8, 5, 2, 9, 5, 6, 3]
// output [2, 3, 5, 5, 6, 8, 9]

function insertSort(array) {
    for(let i = 0; i < array.length; i++) {
        j = i;
        while(j > 0 && array[j] < array[j -1]) {
            swap(j, j -1, array);
            j -= 1;
        }
    }
    return array;
}

function swap(i, j, array) {
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

console.log(insertSort([8, 5, 2, 9, 5, 6, 3]));