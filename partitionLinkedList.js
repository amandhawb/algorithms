// Given a linked list and a value x, rearrange the list such that all nodes with values less than x come before nodes with values greater than or equal to x. 
// Nodes with the value x itself can be anywhere in the second partition. The original order of nodes within each partition must be preserved.


class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

function partitionLinkedList(head, x) {
    console.log("aqui", head);
    const dummyHead = new Node(null);
    dummyHead.next = head;

    let leftTail = dummyHead;
    let curr = head.next;

    while(curr) {
        if(curr.data < x) {
            leftTail.next = curr;
            leftTail = curr;
        }
        curr = curr.next;
    }

    leftTail.next = head;

    console.log("aqui2", head)
    return dummyHead.next;
}

const head = new Node(3);
head.next = new Node(1);
head.next.next = new Node(5);
head.next.next.next = new Node(2);
head.next.next.next.next = new Node(4);

partitionLinkedList(head, 3)

