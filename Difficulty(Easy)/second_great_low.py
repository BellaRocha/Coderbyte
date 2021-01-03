#Second GreatLow

#Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!

#Examples:
#Input: [1, 42, 42, 180] 
#Output: 42 42
#Input: [4, 90] 
#Output: 90 4

#Tags:
#Array
#Searching
#Sorting

#Python:
def SecondGreatLow(arr):
  nodup_list = sorted(list(set(arr)))
  if len(nodup_list) == 1:
    return str(nodup_list[0]) + " " + str(nodup_list[0])
  return str(nodup_list[1]) + " " + str(nodup_list[len(nodup_list) - 2])

# keep this function call here 
print SecondGreatLow(raw_input())
