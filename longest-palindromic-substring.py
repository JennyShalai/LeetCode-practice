# 5. Longest Palindromic Substring
# 

def longestPalindrome(s):
  s2 = list(s)
  s2 = ' '.join(s2)
  s2 = ' ' + s2 + ' '
  longPalindrom = ''
  radius = 0
  center = 0
  for index, char in enumerate(s2):
    i = 0
    while index-i >= 0 and index+i < len(s2) and s2[index-i] == s2[index+i]:
      i += 1
    if i > radius:
      radius = i
      center = index
  longPalindrom = s2[center-radius+1:center+radius:1]
  longPalindrom = longPalindrom.replace(" ", "")
  return longPalindrom

print(longestPalindrome('rqdbdqwtqdbdqt'))
print(longestPalindrome('abbc'))
print(longestPalindrome('abb'))
