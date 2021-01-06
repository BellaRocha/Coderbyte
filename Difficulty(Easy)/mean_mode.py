Mean Mode

Have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). The array will not be empty, will only contain positive integers, and will not contain more than one mode.

Examples:
Input: [1, 2, 3] 
Output: 0
Input: [4, 4, 4, 6, 2] 
Output: 1

Tags:
Array
Math Fundamentals
Hash Table

Python:
def MeanMode(arr):
  mode = 0 
  counter = 0
  for i in range (len(arr)):
    if arr.count(arr[i]) >= counter:
      counter = arr.count(arr[i])
      mode = arr[i]
  
  mean = sum(arr)/len(arr)

  if mode == mean:
    return 1
  else:
    return 0

# keep this function call here 
print MeanMode(raw_input())
