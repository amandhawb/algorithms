class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def get_youngest_common_ancestor(topAncestor, descendantOne, descendantTwo):
    depthOne = get_descendant_depth(descendantOne, topAncestor)
    depthTwo = get_descendant_depth(descendantTwo, topAncestor)

    if depthOne > depthTwo:
        diff = depthOne - depthTwo
        return backtrackAncestralTree(descendantOne, descendantTwo, diff)
    else:
        diff = depthTwo - depthOne
        return backtrackAncestralTree(descendantTwo, descendantOne, diff)

def get_descendant_depth(descendant, topAncentor):
    depth = 0
    while descendant != topAncentor:
        descendant = descendant.ancestor
        depth +=1
    return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -=1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant


# TEST 1:
A = AncestralTree("A")
B = AncestralTree("B")
C = AncestralTree("C")
B.ancestor = A
C.ancestor = A
print(get_youngest_common_ancestor(A, B, C).name) # A

# TEST 2:
D = AncestralTree("D")
E = AncestralTree("E")
F = AncestralTree("F")
G = AncestralTree("G")
H = AncestralTree("H")
E.ancestor = D
F.ancestor = D
G.ancestor = E
H.ancestor = E
print(get_youngest_common_ancestor(D, H, F).name) # D

