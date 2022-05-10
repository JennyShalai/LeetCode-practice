# Plus One
# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits):
  digits = digits[::-1]
  result = []
  addOne = True
  for digit in digits:
    if addOne:
      digit += 1
      if digit < 10:
        addOne = False
        result.append(digit)
      else:
        result.append(digit % 10)
    else:
      result.append(digit)
  if addOne:
    result.append(1)
  return result[::-1]     

print(plusOne([9,9,9,9])) #[1, 0, 0, 0, 0]
