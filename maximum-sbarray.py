# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6

def maxSubArray(nums):
  currentSum = 0
  maxSum = nums[0]
  for n in nums:
    if currentSum < 0:
      currentSum = 0
    currentSum += n
    maxSum = max(currentSum, maxSum)
  return maxSum
