#Letter Capitalize

#Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space.

#Examples:
#Input: "hello world" 
#Output: Hello World
#Input: "i ran there" 
#Output: I Ran There

#Tags:
#String Manipulation

#Python:
def LetterCapitalize(strParam):
  return strParam.title()

# keep this function call here 
print LetterCapitalize(raw_input())

------------------OR------------------

def LetterCapitalize(strParam):
  list_str = strParam.split(' ')
  string_updated = ""
  for i in range (len(list_str)):
    string_updated += list_str[i].capitalize() + ' '

  return string_updated[:-1]

# keep this function call here 
print LetterCapitalize(raw_input())
