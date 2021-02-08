#Trapping Water

#Have the function TrappingWater(arr) take the array of non-negative integers stored in arr, and determine the largest amount of water that can be trapped. The numbers in the array represent the height of a building (where the width of each building is 1) and if you imagine it raining, water will be trapped between the two tallest buildings. For example: if arr is [3, 0, 0, 2, 0, 4] then this array of building heights looks like the following picture if we draw it out: 
https://i.imgur.com/PD6xjHs.png

#Now if you imagine it rains and water gets trapped in this picture, then it'll look like the following (the x's represent water): 
https://i.imgur.com/IL49eNq.png
#This is the most water that can be trapped in this picture, and if you calculate the area you get 10, so your program should return 10.

#Examples:
#Input: [1, 2, 1, 2] 
#Output: 1
#Input: [0, 2, 4, 0, 2, 1, 2, 6] 
#Output: 11

#Tags:
#Amazon
#Array
#Data Engineer
#Google
#Microsoft
#Stack

#Python:

def TrappingWater(arr):
  height = 0
  final_volume = 0
  # code goes here
  for i in range(len(arr)):
    volume = 0
    if arr[i] > height:
      height = arr[i]
    else:
      volume = height - arr[i]
      height = volume + arr[i]
    final_volume += volume
  return final_volume

# keep this function call here 
print TrappingWater(raw_input())
