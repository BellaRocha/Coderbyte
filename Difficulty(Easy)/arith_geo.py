#Arith Geo

#Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.

#Examples:
#Input: [5,10,15] 
#Output: Arithmetic
#Input: [2,4,16,24] 
#Output: -1

#Tags:
#Array
#Math Fundamentals
#Sequences

#Python:
def ArithGeo(arr):
  first = arr[0]
  second = arr[1]
  g = second/first
  a = second - first
  a_check = 2
  g_check = 2

  for i in range (1, len(arr) - 1):
    if arr[i] + a == arr[i + 1]:
      a_check += 1
    elif arr[i] * g == arr[i + 1]:
      g_check += 1
  
  if a_check == len(arr):
    return "Arithmetic"
  elif g_check == len(arr):
    return "Geometric"
  else:
    return -1

# keep this function call here 
print ArithGeo(raw_input())
