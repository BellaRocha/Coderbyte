#Simple Symbols

#Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several characters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter.

#Examples:
#Input: "+d+=3=+s+" 
#Output: true
#Input: "f++d+" 
#Output: false

#Tags:
#Regular Expression
#String Manipulation

#Python:
def SimpleSymbols(strParam):
  if len(strParam) == 1:
    return "false"
  for i in range (len(strParam) - 1):
    if strParam[i].isalpha():
      if i == 0:
        return "false"
      else:
        if strParam[i-1] == '+' and strParam[i + 1] == '+':
          continue
        else: 
          return "false"
  return "true"

# keep this function call here 
print SimpleSymbols(raw_input())
