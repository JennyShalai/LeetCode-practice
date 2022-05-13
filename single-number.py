# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
  tempDict = {}
  for n in nums:
    if n in tempDict:
      del tempDict[n]
    else:
      tempDict[n] = 1
  return list(tempDict.keys())[0]
  
print(singleNumber([1,2,3,4,2,3,1]))
