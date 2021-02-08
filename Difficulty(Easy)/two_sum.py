#Two Sum

#Have the function TwoSum(arr) take the array of integers stored in arr, and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array. For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11]. Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array. Pairs should be separated by a space. So for the example above, your program would return: 5,2 -4,11 

#If there are no two numbers that sum to the first element in the array, return -1

#Examples:
#Input: [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7] 
#Output: 6,11 10,7 15,2
#Input: [7, 6, 4, 1, 7, -2, 3, 12] 
#Output: 6,1 4,3

#Tags:
#Amazon
#Array 
#Dynamic Programming
#Facebook
#Google
#Hash Table
#Searching

#Pyhton:

import itertools

def TwoSum(arr):
  goal = arr[0]
  output = ""
  a = list(itertools.combinations(arr[1:], 2))
  for i in range (len(a)):
    if sum(a[i]) == goal:
      output += str(a[i][0])
      output += ','
      output += str(a[i][1])
      output += ' '
  if len(output) < 1:
    return '-1'
  return output

# keep this function call here 
print TwoSum(raw_input())
