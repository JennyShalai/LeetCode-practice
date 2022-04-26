# Two Sum 
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#DONE  
def twoSum(nums, target):
  dict = {}
  for index, n in enumerate(nums):
    if n in dict:
      return [index, dict[n]]
    else:
      dict[target-n] = index
  return []      

print(twoSum([1,2,3,4,5,6,7,8,9], 10)) #[5, 3]
