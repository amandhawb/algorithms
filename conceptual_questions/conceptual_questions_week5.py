def quiz(i):
    if i > 1:
        quiz(i/2)
        quiz(i/2)
    print('*')

# 1) How many asterisks are printed by the method call quiz(5)?
quiz(5)

def test_a(n):
    print(({n}))
    if n > 0:
        test_a(n-2)

# 2) What is printed by the call test_a(4)? 
test_a(4)

def test_b(n):
    if n > 0:
        test_b(n-2)
        print(({n}))

# 3) What is printed by the call test_b(4)?
test_b(4)

