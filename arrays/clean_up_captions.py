# As a developer, you're working on a project to dean up captions and optimize storage. With millions of captions and hashtags circulating the platform, your task is to detect any overlap between captions on the for you feed and the following feed. But it's not just about finding common words or hashtags, you need to identify any common substring between the two.
# You are given two lists of captions - one from the for you feed and another from the following feed. For each corresponding pair of captions, your job is to check if any substring appears in both captions. If a common substring is found, you should output YES"; otherwise, output "NO."
from collections import defaultdict

def clean_up_captions(arr1, arr2):
    map_chars = defaultdict(list)

    for i in range(len(arr1)):
        for char in arr1[i]:
            map_chars[i].append(char)

    # map_chars = {
    #   0: [b,a],
    #   1: [m,d],
    #   2: [r,j]
    # }

    for i in range(len(arr2)):
        for char in arr2[i]:
            if char in map_chars[i]:
                print("YES")
                break
            else:
                print("NO")
                break

clean_up_captions(["ba", "md", "rj"], ["af", "ee", "rf"]) # YES NO YES

# VISUAL:
# 1st: 
# i = 0
# char = b
# map_chars = {
#   0: [b]
# }
# char = a
# map_chars = {
#   0: [b,a]
# }

# 2nd: 
# i = 1
# char = m
# map_chars = {
#   0: [b,a],
#   1: [m]
# }
# char = d
# map_chars = {
#   0: [b,a],
#   1: [m,d]
# }

# 3rd: 
# i = 2
# char = r
# map_chars = {
#   0: [b,a],
#   1: [m,d],
#   2: [r]
# }
# char = j
# map_chars = {
#   0: [b,a],
#   1: [m,d],
#   2: [r, j]
# }