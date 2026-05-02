# O in O(n) means the WORST possible scenario, not average (theta) nor the best (omega)

# O(n) ALGORITHM
def print_items(n):
  for i in range(n):
    print(i)
print_items(3) 

# O(n^2) ALGORITHM
# used to compare 2 things in brute-force manner
# for the example below it's called O(a * b) algorithm not O(n^2)
def compare_print(a, b):
  for i in range(a):
    for j in range(b):
      print(j,i)      
compare_print(3)

# O(1) ALGORITHM
# the most efficient algorithm
def add_items(n):
  # This is O(1) no matter how much added:
  return n + n + n # + ... 
add_items(3) 
