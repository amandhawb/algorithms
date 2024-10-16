# https://www.hackerrank.com/challenges/qheap1/problem
# This question is designed to help you get a better understanding of basic heap operations.
# There are 3 types of query:

# "1 v" - Add an element v to the heap.
# "2 v" - Delete the element v from the heap.
# "3" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.


# time = O(n) -> because of .remove() and .heapify() and O(log n) for insertion
# space = O(n) -> where n is the number of elements in the heap
import heapq
n = int(input())
my_heap = []

for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(my_heap, query[1])
    elif query[0] == 2:
        my_heap.remove(query[1]) # it takes O(n)
        heapq.heapify(my_heap)
    elif query[0] == 3:
        print(my_heap[0])