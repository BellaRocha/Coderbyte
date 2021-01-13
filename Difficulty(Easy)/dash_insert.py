#Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

#Examples:
#Input: 99946 
#Output: 9-9-946
#Input: 56730 
#Output: 567-30

#Tags:
#Searching
#String Manipulation

#Python:

def DashInsert(strParam):
  odd = 0
  final_str = ""
  for i in strParam:
    if int(i) % 2 != 0:
      odd += 1
    if int(i) % 2 == 0:
      odd = 0
    if odd == 2:
      final_str += "-"
      odd = 1
    final_str += i

  return final_str

# keep this function call here 
print DashInsert(raw_input())

