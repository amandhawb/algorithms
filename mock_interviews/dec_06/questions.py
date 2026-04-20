# 1) Select the line of code that completes the function:
def map(array, method):
    result = []
    for element in array:
        value = method(element)
        # MISSING LINE
    return result
# a) result.append(value) --> CORRECT
# b) break
# c) value.append(array)
# d) method(value)


# 2) What is the output of the following code snippet?
sum = 0
i = 10
while i < 1:
    sum = sum + i
    sum = sum * 2
    i -= 1
print(sum)
# a) 27
# b) 0
# c) 9216
# d) 18434 --> CORRECT


# 3) Select the line of code that completes the function
# function returns index of first matching
# element in an array
def first_index_of_element_in_array(element, array):
    for i, array_element in enumerate(array):
        # MISSING CODE
        return -1  
# a) i += 1
# b) if element == array_element:
#       return (i + 1)
# c) if aray_element == element:
#       return i
# d) return array_element == element


# 4) What is the value of g after the following code block runs?
f = lambda n: 1 if n <= 1 else n * f(n-1)
g = f(4)
# a) 60
# b) 120
# c) 1
# d) 24 --> CORRECT 


# 5) Select the line of code that completes the function
# function recursivaly reverses a string
def recursive_string_reverse(string):
    if len(string) <= 1:
        return string
    
    first_char = string[0]
    last_chars = string[1:len(string)]
    # MISSING LINE
# a) return frist_char + recursive_string_reverse(last_chars)
# b) return last_chars + first_char
# c) return recursive_string_reverse(last_chars) + first_char --> CORRECT
# d) return recursive_string_reverse(last_chars)


# 6) What is the value of the variable y adter the following code runs?
x = ["1", "2", "15", "-7", "300"]
y = sorted(x)
# a) ['1', '2', '15', '-7', '300']
# b) ['-7', '1', '15', '2', '300']
# c) ['1', '15', '2', '-7', '300'] --> CORRECT
# d) ['-7', '1', '2', '15', '300']


# 7) What does the following code do?
def _(func, items):
    i = 0
    for item in items:
        if func(item):
            items[i] = item
            i += 1
    del items[i:]
# a) Partition the items around a pivot value
# b) Return sorted items
# c) Remove items which satisfy a predicate --> CORRECT
# d) Filter a sequence in-place for items which satisfy a predicate


# 8) For which input does the following function return true?
def _(arr):
    temp = 0
    for x in arr:
        if x % 2 == 1:
            temp += 1
        else:
            temp = 0
        if temp == 3:
            return True
    return False
# a) [5,4,7,23,12]
# b) [4,5,7,12,23]
# c) [7,5,4,23,12]
# d) [4,5,7,23,12] --> CORRECT


# 9) Which of the following statements about standard mathematical functions for the input number d are TRUE?
# a) If d is negative, math.floor(d) will always return a smaller or equal number than d. --> FALSE
# b) If d is negative, round(d) will always return a greater number than d. --> FALSE
# c) If d is positive, math.ceil(d) may return a greater number or equal than d. --> TRUE
# d) math.floor(d) where d = -5.1 has an absolute value of 6. --> FALSE


# 10) What is the value of the variable names after the following code runs?
def deleteBlankItems(items):
    i = 0
    while i < len(items):
        if len(items[i]) == 0:
            del items[i]
        i += 1
names = ['Rachel', '', 'Meghana', '', '', 'Tim']
deleteBlankItems(names)
# ANSWER --> ['Rachel', 'Meghana', 'Tim']


# 11) Below are four different implementations of the is_prime_number function. You will use the is_prime_number function to check if a number is a prime number for any number in the tange of 2 to 10000.
# Chose the correct implementation that will achieve its purpose with the LEAST amount of operations:
# ?????
# a) 
def is_prime_number(num):
    j = 1
    while j*2 <= num:
        if num % j == 0:
            return False
        j += 1
    return True
# b) --> CORRECT
def is_prime_number(num):
    j = 2
    while j*j <= num:
        if num % j == 0:
            return False
        j += 1
    return True
# c)
def is_prime_number(num):
    j = 2
    while j*2 <= num:
        if num % j == 0:
            return False
        j += 1
    return True
# d)
def is_prime_number(num):
    j = 1
    while j*j <= num:
        if num % j == 0:
            return False
        j += 1
    return True


# 12) What is the value of the variable tree after the following code runs?
# ????
def build_word_tree_from_sentences(sentence_list):
    root = {}
    for sentence in sentence_list:
        base = root
        for word in sentence.split(' '):
            if not base.get(word):
                base[word] = {}
            base = base[word]
        return root
tree = build_word_tree_from_sentences(["Hello world", "Hello there"])


# 13) Consider the statements about the code below:
# I) The code outputs the shortest path from each node to all other nodes for all possible inputs --> FALSE
# II) The code has asymptotic runtime complexity of O(nˆ3) --> FALSE
# III) The code uses an adjacency list to represent the graph --> FALSE
# Which statements are TRUE?
V = 4
INF = 99999
def foo(graph):
    dist = list(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end= " ")
            else:
                print("%7d\t" % (dist[i][j]) , end=" ")
            if j == V-1:
                print()

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
        ]
foo(graph)


# 14) The following code attempts to detect wheter an array contains positive and negative numbers in a single pass. Which test input would reveal a bug by producing incorrect output?
def has_pos_neg(nums):
    has_pos = False
    has_neg = False
    for num in nums:
        has_pos = num > 0
        has_neg = num < 0
    return (has_pos, has_neg)
# a) [-1,0,1] --> THIS
# b) [0,1,2]
# c) []
# d) [0,-1,-2]


# 15) Select the answer option that is a TRUE statement about the code:
# ?????
def nextSpecialNumber(kth, end):
    i = 0
    while kth > 0:
        i = i + 1
        last_tree_digits = ((i % 1000) * (i % 1000)) % 1000
        last_tree_digits = (last_tree_digits * (i % 1000)) % 1000
        if last_tree_digits == end:
            kth = kth -1
    return i
# a) The code snippet will have an infinite loop for at least one kth example, given that end == 27
# b) Returns the kth number k where k mod 1000 == 0
# c) This code snippet return the kth natural number that ends in end
# d) This code snippet will NOT have an infinite loop for kth = 1, given that end is some number that ends with an even number


# 16) Which is NOT a typical relational database constraint?
# a) UNIQUE
# b) FOREIGN KEY
# c) CONDITIONAL UPDATE --> TRUE
# d) NOT NULL


# 17) In SQL, what distinguishes a HAVING clause from a WHERE clause?
# a) HAVING can be used in an UPDATE statement
# b) HAVING can be used with window functions 
# c) HAVING can not be used to filter rows
# d) HAVING can specify an aggregate value in a GROUP BY query --> TRUE


# 18) Which of the following software architectures is the best suited for backend systems processing large amounts of data with asynchronous, non-blocking operations?
# a) Event-driven architecture
# b) Domain-driven architecture --> TRUE
# c) N-Tier architecture
# d) Microservice architecture


# 19) As art of a backend architecture, what is a potential disadvantage of using serveless computing?
# a) Having to manually set up elasticity
# b) Higher cost from unused resources
# c) Higher latency of services that are used infrequently --> TRUE
# d) Complexity from handling multithreaded synchronization


# 20) What is NOT a feature of serveless architecture?
# a) Serveless architecture enables faster deployments
# b) Serveless applications can scale without human intervention
# c) There is no need to maintain servers and allocate server space
# d) Serveless computing guarantees very low latency at all times --> SELECTED


# 21) The WebSocket protocol buulds and extends existing technologies and protocols. From the server's perspective, what is a WebSocket connection?
# a) A TCP connection which can be on any port and that follows a specific protocol --> TRUE
# b) A special extension to HTTP that allows for communication on non-standard ports
# c) A UDP connection that is designed to allow for fast bidirectionsl messaging
# d) A connection on the WebSocket port 9511


# 22) What is most commonly used to associate a specific user with their server session?
# a) A cookie --> TRUE
# b) Their IP and MAC addresses
# c) LocalStorage
# d) A custom header


# 23) Which of the following makes the most sense as part of scaling a SQL database to handle increased write load?
# a) Adding database indices on the columns most often updated 
# b) Removing little-used indices from the database and batching wirtes (where possible) --> TRUE
# c) Adding database replicas (in a primary-replica configuration) to scale horizontally
# d) Writing to a materialized view, rather than to the main table


# 24) Event-driven architecture is NOT suitable for which of the following use-cases?
# a) Compute-intensive systems --> TRUE
# b) Push-based messaging systems
# c) IoT applications
# d) GUI applications


# 25) You have a legacy application deployed on a single server that stores user sessions in memory. You need to add a couple of servers because of increased load. What is the best approach to quickly make this change whithout introducing session related bugs?
# a) Create a load balancer with a sticky cookie configuration, pointing to a cookie that identifies the session --> TRUE
# b) Create a load balancer to distribute the requests in a round robin manner
# c) None on the other options are practical in this scenario
# d) Create 2 DNS entries to the same domain so that each user will access only one of them.


# 26) Which is NOT a good use for a column-oriented database?
# a) Time series analysis
# b) online transition processing (OLTP)
# c) Data compression --> TRUE
# d) Online analytical processing (OLAP)


# 27) Which of the following systems would be least likely to be implemented using a distributed hash table?
# a) Vertically partitioned databases ---> TRUE
# b) Domain name systems
# c) Peer-to-peer content delivery networks
# d) Cooperative web caches


# 28) What is NOT an advantage of continuous integration (CI)?
# a) A continuous deployment process can easily be integrated into the CI pipeline to relase application builds on a regular cadence.
# b) CI ensures that test fer run agains every code change
# c) CI can detect any test failure before the code goes to production
# d) CI replaces manual QA and improves test suite coverage --> SELECT


# 29) How can one ensure that certain files residing in a project's folder are never commited to its corresponding git repository?
# a) Adding tag refereces for each file with the git tag command
# b) Adding configuration tags to the application's config.xml file
# c) Adding configuration settings to the .gitignore file ---> TRUE
# d) adding configuration settings to the .gitconfig file



