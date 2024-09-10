# Imagine we are a software development company and we manage our dev process using an issue tracking tool. Each issue has an ID and also a list of IDs of issues which block it (Blockers or parents). As a result we have 1 or multiple unidirectional graphs because there could have several root issues (Epics).
# At some point in time someone added an issue A as a Blocker of issue B. But because A was already blocked by the descendants of the current issue B (descendants of B are the issues that are transitively blocked by B), this created a circular dependency. After this our UI issue tracking tool (Taskflow) stopped showing issues correctly. Our task is to find out all circular dependency loops.

# The input is a 2D boolean array of blockers assignments. The row number is the issue ID. The column number is Blocker issue ID. So entry (i, j) is True means that issue i is blocked by issue j.
# Example input:
# - 0 1 2
# 0 False False True 
# 1 True False False
# 2 False True False

# 2 -> 0 -> 1 -> 2

# The output is a list of dependency cycles. The order inside one cycle doesn't matter.
# Example:
# [
# [0, 2, 1] (as well can be 2,1,0 or 1,0,2)
# ]

def finding_cycles(issues):
    num_of_issues = len(issues) -1 # disconsidering first (head) row
    issues_hash_map = { i: [] for i in range(num_of_issues) }

    # build hash map
    for row in range(1, num_of_issues +1):
        for col in range(1, num_of_issues +1):
            if issues[row][col]:
                issues_hash_map[row-1].append(col-1)
    
    already_seen = set()
    cycles = []
    # verify cycle
    def dfs(issue, recursion_stack):
        if issue in recursion_stack:
            cycle_start = recursion_stack.index(issue)
            cycles.append(recursion_stack[cycle_start:])
            return True
        if issue in already_seen:
            return False
        already_seen.add(issue)
        recursion_stack.append(issue)

        for blocker in issues_hash_map[issue]:
            if dfs(blocker, recursion_stack):
                return True
        
        recursion_stack.pop()
        return False
    
    for issue in range(num_of_issues):
        if issue not in already_seen:
            dfs(issue, [])
    return cycles

matrix1 = [
    ['-', 0, 1, 2],
    [0, False, False, True],
    [1, True, False, False],
    [2, False, True, False]
]

matrix2 = [
    ['-', 0, 1, 2],
    [0, False, False, True],
    [1, False, False, False],
    [2, False, True, False]
]

matrix3 = [
    ['-', 0, 1],
    [0, False, True],
    [1, True, False]
]

print(finding_cycles(matrix1)) # [[0,2,1]]
print(finding_cycles(matrix2)) # []
print(finding_cycles(matrix3)) # [[0,1]]
