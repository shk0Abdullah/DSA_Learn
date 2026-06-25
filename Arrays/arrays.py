# In python you dont have true static arrays 

nums = [12,12,3,4] # -> Dynamic Array

# Preallocated memory for later use but not the true static arr
arr = [0] * 5 

arr.append(12)
# comments Handwritten ha 
# when you append from the last you append the memory address and had the complexity of O(1)
# but if you append it from top this would be O(n) cause in array shift would happen in the memory
# that's the exact reason why python does not have a function append From top 

# although we have the insert func its complexity is O(n)
# cause it does doing the shift for the insertion at specific index

arr.pop(0) 

print(arr)

# We have tuples to cover the atatic arr scenerio in python

tup = (1,2,3)

