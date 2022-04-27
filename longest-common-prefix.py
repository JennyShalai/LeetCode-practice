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
