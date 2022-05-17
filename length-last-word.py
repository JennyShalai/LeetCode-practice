# Length of Last Word: Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def LengthOfLastWord(s):
  index = len(s) - 1
  k = 0
  while s[index] == ' ':
    index -= 1
  while index >= 0 and s[index] != ' ':
    k += 1
    index -= 1
  return k

# with built-in functions
def lengthOfLastWord2(s):
  s = s.strip()
  sArr = s.split(sep=' ')
  return len(sArr[-1])

# algorithmic approach
def lengthOfLastWord3(s):
  s = s[::-1].strip()
  result = 0
  for char in s:
    if char == ' ':
      return result
    else:
      result += 1
  return result
