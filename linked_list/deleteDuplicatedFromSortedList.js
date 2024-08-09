// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
// Return the linked list sorted as well.
//exemple: 
// input: 1 --> 1 --> 2
// output 1 --> 2

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

// space: O(1)
// time: O(n)
function deleteDuplicated(list) {
    if(list == null) {
        return null
    }

    let current = list;
    while(current.next != null) {
        if(current.val == current.next.val) {
            let next_next = current.next.next;
            let nodeToDelete = current.next;
            delete(nodeToDelete);
            current.next = next_next;
        } else {
            current = current.next;
        }
    }
    return list;
}

