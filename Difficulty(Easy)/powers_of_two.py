#Powers of Two

#Have the function PowersofTwo(num) take the num parameter being passed which will be an integer and return the string true if it's a power of two. If it's not return the string false. For example if the input is 16 then your program should return the string true but if the input is 22 then the output should be the string false.

#Examples:
#Input: 4 
#Output: true
#Input: 124 
#Output: false

#Tags:
#Math Fundamentals
#Google

#Python:

import math

def PowersofTwo(num):
  return math.log(num, 2).is_integer()

# keep this function call here 
print PowersofTwo(raw_input())
