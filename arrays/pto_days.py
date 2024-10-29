# You're given a list of days represented as a char array that contains either H or W where:
# H = Holiday
# W = Workday
# Given a number of Personal Time-Off days (PTO), maximize the length of the longest vacation you can take.

# [W, H, H, W, W, H, W], PTO = 2 --> Your maximum vacation is 5 days.

def longest_vacation(days, pto):
    max_vacation = 0
    left = 0
    workdays_used = 0

    for right in range(len(days)):
        if days[right] == 'W':
            workdays_used += 1
        
        while workdays_used > pto:
            if days[left] == 'W':
                workdays_used -= 1
            left += 1
        
        max_vacation = max(max_vacation, right - left + 1)
    
    return max_vacation

days = ['W', 'H', 'H', 'W', 'W', 'H', 'W']
print(longest_vacation(days, 2)) # 5

