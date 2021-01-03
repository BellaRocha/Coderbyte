#Counting Minutes I

#Have the function CountingMinutesI(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.

#Examples:
#Input: "12:30pm-12:00am" 
#Output: 690
#Input: "1:23am-1:08am" 
#Output: 1425

#Tags:
#Searching
#String Manipulation

#Python:

import datetime
def CountingMinutesI(strParam):
  list_time = strParam.split('-')
  first_time = list_time[0]
  second_time = list_time[1]
  if len(first_time) < 7:
    first_time = "0" + first_time
  if len(second_time) < 7:
    second_time = "0" + second_time 

  def convert24 (time):
    if time.count('am') == 1 and time.count('12') == 1:
      return "00:00"
    elif time.count('am') == 1:
      return time[0:-2]
    elif time.count('pm') == 1 and time.count('12') == 1:
      return time[0:-2]
    else:
      return str(int(time[0:2]) + 12) + time[2:-2]

  FMT = '%H:%M'

  t1 = datetime.datetime.strptime(convert24(first_time), FMT)
  t2 = datetime.datetime.strptime(convert24(second_time), FMT)

  td = t2 - t1
  answer = td.seconds/60

  return answer

# keep this function call here 
print CountingMinutesI(raw_input())
