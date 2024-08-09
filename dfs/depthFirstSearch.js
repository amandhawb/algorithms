// given a node class that has a name and an array of optional children nodes. When put together, nodes form an acyclick tree-like structure.
// implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the DFS approach.

class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(node) {
    this.children.push(node)
  }
  
  // SECOND TIME:
  depthFirstSearch(array) {
    array.push(this.name);
    for(let i = 0; i < this.children.length; i++) {
      let currentChild = this.children[i];
      currentChild.depthFirstSearch(array);
    }
  }

    // depthFirstSearch(array) {
    //   array.push(this.name);
    //   for(let i = 0; i < this.children.length; i++) {
    //     this.children[i].depthFirstSearch(array);
    //   }
    //   return array;
    // }
}

const root = new Node("A");
const B = new Node("B");
const C = new Node("C");
const D = new Node("D");

root.addChild(B);
root.addChild(C);
root.addChild(D);

const E = new Node("E");
const F = new Node("F");
const G = new Node("G");
const H = new Node("H");

B.addChild(E);
B.addChild(F);

D.addChild(G);
D.addChild(H);

const I = new Node("I");
const J = new Node("J");
const K = new Node("K");

F.addChild(I);
F.addChild(J);

G.addChild(K);

let response = [];
root.depthFirstSearch(response);
console.log(response);
