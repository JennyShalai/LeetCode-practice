# Sort colors
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
def sortColors(arr):
  dict = {}
  result = []
  #counting how many each color appears 
  for i in arr:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  #forming output for each color
  for j in range(3):
    for k in range(dict[j]):
      result.append(j)
  return result
print(sortColors([2,0,2,1,1,0]))
