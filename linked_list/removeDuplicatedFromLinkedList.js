// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
// Return the linked list sorted as well.
// input: 1 --> 1 --> 2
// output: 1 --> 2

// Definition for singly-linked list.
// function ListNode(value, next) {
//     this.value = (val===undefined ? 0 : value)
//     this.next = (next===undefined ? null : next)
// }

function removeDuplicatedFromLinkedList(head) {
    if(head == null) {
        return false;
    }

    let current = head;
    while(current.next != null) {
        if(current.value == current.next.value) {
            let next_next = current.next.next;
            let nodeToDelete = current.next;
            delete(nodeToDelete);
            current.next = next_next;
        } else {
            current = current.next;
        }
        
    }
    return head;
}
