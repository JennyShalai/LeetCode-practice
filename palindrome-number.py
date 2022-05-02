# 9. Palindrome Number

# cast to string
def isPalindrome1(n: int):
  digits = str(n)
  for i in range((len(digits))//2):
    if digits[i] != digits[(len(digits))-1-i]:
      return False
  return True

def isPalindrome2(x):
  return False if x < 0 else str(x)[::-1] == str(x)

# math approach (no cast)
def isPalindrome3(x):
  if x < 0:
    return False
  y = x
  xRever = 0
  while y > 0:
    xRever = xRever * 10 + y % 10
    y = y // 10
  return xRever == x

print(isPalindrome3(123))
