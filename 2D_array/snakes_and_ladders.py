# https://www.hackerrank.com/challenges/the-quickest-way-up/problem
# https://leetcode.com/problems/snakes-and-ladders/description/

from collections import deque
class Solution:
    def snakesAndLadders(self, board):
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r,c]
        
        q = deque()
        q.append([1,0]) # [square, moves]
        visit = set()

        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = intToPos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == length * length:
                    return moves + 1
                if next_square not in visit:
                    visit.add(next_square)
                    q.append([next_square, moves + 1])
        return -1