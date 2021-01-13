#Have the function SwapCase(str) take the str parameter and swap the case of each character. For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are.

#Examples:
#Input: "Hello-LOL" 
#Output: hELLO-lol
#Input: "Sup DUDE!!?" 
#Output: sUP dude!!?

#Tags:
#String Manipulation

#Python:

def SwapCase(strParam):
  final = ""
  for i in strParam:
    if i.isupper():
      final += i.lower()
    elif i.islower():
      final += i.upper()
    else:
      final += i

  return final

# keep this function call here 
print SwapCase(raw_input())
