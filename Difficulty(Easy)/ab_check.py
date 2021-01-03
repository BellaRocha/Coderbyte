#AB Check

#Have the function ABCheck(str) take the str parameter being passed and return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false.

#Examples:
#Input: "after badly" 
#Output: false
#Input: "Laura sobs" 
#Output: true

#Tags:
#Regular Expression
#String Manipulation

#Python:
def ABCheck(strParam):
  i = 0
  pair = 0
  while i < (len(strParam) - 4):
    if strParam[i] == 'a':
      if strParam[i + 4] == 'b':
        pair += 1
    if strParam[i] == 'b':
      if strParam[i + 4] == 'a':
        pair += 1
    i += 1
  if pair >= 1:
    return "true"
  return "false"
  
# keep this function call here 
print ABCheck(raw_input())
