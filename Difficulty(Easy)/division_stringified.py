#Division Stringified

#Have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas. If an answer is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346".

#Examples:
#Input: 5 & num2 = 2 
#Output: 3
#Input: 6874 & num2 = 67 
#Output: 103

#Tags:
#Math Fundamentals

#Python:
def DivisionStringified(num1,num2):
  div = float(num1)/float(num2)
  rounded_div = int(round(div))
  str_div = str(rounded_div)
  if rounded_div > 999:
    other_div = ""
    comma = 0
    for i in range ((len(str_div) - 1), -1, -1):
      other_div += str_div[i]
      comma += 1
      if comma % 3 == 0:
        other_div += ','
    return other_div[::-1]
    
  return str_div

# keep this function call here 
print DivisionStringified(raw_input())
