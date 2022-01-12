# Write a Python program to create an intersection, Union, difference of sets.
# 20CE007 Jatan Bhimani


d = {0, 2, 4, 6, 8};
d1 = {1, 2, 3, 4, 5};
  
# union
print("Union :", d | d1)
  
# intersection
print("Intersection :", d & d1)
  
# difference
print("Difference :", d - d1)
  
# symmetric difference
print("Symmetric difference :", d ^ d1)