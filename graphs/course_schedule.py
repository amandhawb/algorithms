# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

def canFinish(numCourses, prerequisites):
    # build a hash map with the courses that are prequisites for each course
    pre_req_map = { i: [] for i in range(numCourses)}
    for course, req in prerequisites:
        pre_req_map[course].append(req)
    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if pre_req_map[course] == []:
            return True
        visited.add(course)

        for req in pre_req_map[course]:
            if not dfs(req): return False
        visited.remove(course)
        pre_req_map[course] = []
        return True
    
    for course in range(numCourses):
        if not dfs(course): return False
    return True


# TEST

print(canFinish(5, [[1,4], [2,4], [3,1], [3,2]])) # true
print(canFinish(2, [[0,1], [1,0]])) # false
print(canFinish(2, [[1,0]])) # true

    