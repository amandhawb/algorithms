# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

def guess(myGuess, pick):
    if myGuess == pick:
        return 0
    if myGuess > pick:
        return -1
    else:
        return 1

def guessNumber(n, pick):
    left, right = 1, n

    while left <= right:
        middle = (left + right) // 2
        if guess(middle, pick) == 0:
            return middle
        elif guess(middle, pick) == -1:
            right = middle - 1
        else:
            left = middle + 1

print(guessNumber(1,1))
print(guessNumber(10,6))
print(guessNumber(2,1))
print(guessNumber(2,2))
    