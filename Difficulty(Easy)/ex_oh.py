#Ex Oh

#Have the function ExOh(str) take the str parameter being passed and return the string true if there is an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

#Examples:
#Input: "xooxxo" 
#Output: true
#Input: "x" 
#Output: false

#Tags:
#Searching
#String Manipulation

#Python:
def ExOh(strParam):
  list_str = list(strParam)
  x_count = list_str.count('x')
  o_count = list_str.count('o')
  if x_count == o_count:
    return "true"
  return "false"

# keep this function call here 
print ExOh(raw_input())
