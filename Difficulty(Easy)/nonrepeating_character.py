#Nonrepeating Character

#Have the function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only alphabetic characters and spaces, and return the first non-repeating character. For example: if str is "agettkgaeee" then your program should return k. The string will always contain at least one character and there will always be at least one non-repeating character.

#Examples:
#Input: "abcdef" 
#Output: a
#Input: "hello world hi hey" 
#Output: w

#Tags:
#Amazon
#Hash Table
#Microsoft
#Searching

#Python: 
def NonrepeatingCharacter(strParam):
  for i in range (len(strParam)):
    if strParam.count(strParam[i]) == 1:
      return strParam[i]

  return strParam[0]

# keep this function call here 
print NonrepeatingCharacter(raw_input())
