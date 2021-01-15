#Third Greatest

#Have the function ThirdGreatest(strArr) take the array of strings stored in strArr and return the third largest word within it. So for example: if strArr is ["hello", "world", "before", "all"] your output should be world because "before" is 6 letters long, and "hello" and "world" are both 5, but the output should be world because it appeared as the last 5 letter word in the array. If strArr was ["hello", "world", "after", "all"] the output should be after because the first three words are all 5 letters long, so return the last one. The array will have at least three strings and each string will only contain letters.

#Examples:
#Input: ["coder","byte","code"] 
#Output: code
#Input: ["abc","defg","z","hijk"] 
#Output: abc

#Tags:
#Array
#Searching
#Sorting

#Python:

def ThirdGreatest(strArr):
  str_length = []
  for word in strArr:
    str_length.append(len(word))

  ordered = sorted(str_length)
  ordered = list(set(ordered))

  if len(ordered) < 3:
    third_greatest = ordered[0]
  else:
    third_greatest = ordered[-3]

  largest_length = [i for i, e in enumerate(str_length) if e == third_greatest]

  return strArr[largest_length[-1]]

# keep this function call here 
print ThirdGreatest(raw_input())
