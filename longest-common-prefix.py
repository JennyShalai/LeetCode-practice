# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Two approaches, leetcode shows the same time and memory efficiency for several submissions

# Take first string of a given array as a prefix
# Go through array and compare prefix with each string and modify prefix accordingly
def longestPrefix(strs):
  prefix = ''
  temp = ''
  if len(strs) == 1:
    return strs[0]
  prefix = strs[0]
  for word in strs:
      print(prefix, word)
      for i in range(min(len(prefix), len(word))):
        if prefix[i] == word[i]:
          temp += prefix[i]
        else:
          break
      prefix = temp
      temp = ''
      print(prefix)
  return prefix

print(longestPrefix(["flower","flow","flight"]))

# For each char in the first string, go through a given array of strings and
# compare with each char at the same char position
def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = ''
    if len(strs) <= 1:
        return strs[0]
    index = 0
    for char in strs[0]:
        for s in strs:
            if index >= len(s) or s[index] != char:
                return prefix
        prefix += char
        index += 1
    return prefix
