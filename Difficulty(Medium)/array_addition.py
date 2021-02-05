#Array Addition

#Have the function ArrayAddition(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array (excluding the largest number) can be added up to equal the largest number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers.

#Examples:
#Input: [5,7,16,1,2] 
#Output: false
#Input: [3,5,-1,8,12] 
#Output: true

#tags:
#Amazon
#Array
#Dynamic Programming
#Facebook
#Google
#Microsoft
#Recursion
#Searching

#Python:

import itertools
import numpy as np

def ArrayAddition(arr):
  largest_number = max(arr)
  test = np.sort(arr)
  cut = test[:-1].copy()
  a = []
  for i in range (1, len(cut) + 1):
    a += list(itertools.combinations(cut, i))

  for j in range (len(a)):
    if len(a[j]) > 1:
      if sum(a[j]) == largest_number:
        return 'true'
  
  return 'false'

# keep this function call here 
print ArrayAddition(raw_input())
