#Letter Changes

#Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

#Examples:
#Input: "hello*3" 
#Output: Ifmmp*3
#Input: "fun times!" 
#Output: gvO Ujnft!

#Tags:
#String Manipulation

#Python:
def LetterChanges(strParam):
  i = 0
  vowels = ['a', 'e', 'i', 'o', 'u']
  new_string = ""
  char = ''
  for i in range (len(strParam)):
    if (strParam[i].isalpha()):
      letter = (chr(ord(strParam[i]) + 1))
      if (letter in vowels):
        new_string += (letter.upper())
      else:
        new_string += letter
    else:
      new_string += strParam[i]

  return new_string

# keep this function call here 
print LetterChanges(raw_input())
