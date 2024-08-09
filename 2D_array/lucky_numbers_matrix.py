# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order. 
# Lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column

def lucky_numbers(matrix):
    lucky_nums = []

    for row in range(len(matrix)):
        min_val = min(matrix[row])
        min_col = matrix[row].index(min_val)

        is_lucky =  True
        for col in range(len(matrix[0])):
            if matrix[col][min_col] > min_val:
                is_lucky = False
                break
        
        if is_lucky:
            lucky_nums.append(min_val)
    
    return lucky_nums