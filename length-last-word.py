# Length of Last Word: Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# with built-in functions
def lengthOfLastWord2(s):
  s = s.strip()
  sArr = s.split(sep=' ')
  return len(sArr[-1])
