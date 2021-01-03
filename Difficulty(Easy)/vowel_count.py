#Vowel Count

#Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge.

#Examples:
#Input: "hello" 
#Output: 2
#Input: "coderbyte" 
#Output: 3

#Tags:
#Regular Expression
#Searching
#String Manipulation

#Python:
def VowelCount(strParam):
  lower_str = strParam.lower()
  count = 0

  for vowel in "aeiou":
    count += lower_str.count(vowel)
  
  return count

# keep this function call here 
print VowelCount(raw_input())
