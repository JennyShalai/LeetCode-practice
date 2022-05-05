# Implement strStr()
# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

def strStr(haystack, needle):  
  if haystack is None or needle is None:
    return -1
  if len(needle) > len(haystack):
    return -1
  for index in range(len(haystack)):
    if haystack[index] == needle[0]:
      i = index
      for char in needle:        
        if i > len(haystack)-1:
          return -1
        if char == haystack[i]:
          i += 1
        else:
          break
        if i - index == len(needle):
          return index   
  return -1
print(strStr('heluuulo', 'lop')) # -1
