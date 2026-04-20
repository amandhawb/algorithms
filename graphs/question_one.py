"""
Your task is to write a function that given a distance d and a stream of floating point values received one at a time, 
checks for groups of three values that are within at most d distance. 
As values are received they should be stored in memory. 
Whenever any group is found meeting the distance criteria, return the three values and remove them from memory.

for a triple (a, b, c) and a distance d, |a-b| <= d AND |b-c| <= d AND |a-c| <= d

d = 2

9 -> (): memory = [9]
10 -> (): memory = [9, 10]
-1.5 ->(): memory = [9, 10, -1.5]
11 -> (9, 10, 11): memory = [-1.5]
12 -> (): memory = [-1.5, 12]
13 -> (): memory = [-1.5, 12, 13]
-2.5 -> (): memory = [-1.5, 12, 13, -2.5]
100 -> (): memory = [-1.5, 12, 13, -2.5, 100]

[100, 13, 14, 12, -1.5, -2.5]

14 -> (12, 13, 14): memory = [100, -1.5, -2.5]

"""

memory = []


"""
d = 2

memory: [2, 6]

4 -> [2, 4, 6]
"""
# Returns the same value every time
def get_distance() -> Float:
  pass

def check_value(f: float) -> Tuple[float]:
  memory.append(f)
  distance = get_distance()
  result = []
  for element in memory:
    if abs(f - element) > distance:
      continue
    else:
      if len(result) == 3:
        
        return result
      for num in result:
        memory.remove(num)
      else:
        result.append(element)
       
      
  
  
  
  
  # Understanding:
  # I will receive a number
    # first thing is store this number in the memory
    # check memory 
      # if len(memory) > 2
        # I will check if the triple is valid
          # one element minus another element needs to be smaller or equal to d
        # return the sub set that meets the criteria
         
  
  # Match:
    # use an array to store the triple (which will be the result)
    # use an array to store the elements (which will be the memory)
    
  