
# Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

def majorityElement(nums):
  majority = len(nums) / 2
  tempDict = {}
  for n in nums:
    if n in tempDict:
      tempDict[n] += 1
    else:
      tempDict[n] = 1
  for number, count in tempDict.items():
    if count > majority:
      return number

print(majorityElement([2,2,1,1,1,2,2])) #2
