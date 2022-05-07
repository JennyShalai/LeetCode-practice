# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.

def isValidParentheses(s):
  if len(s) % 2 != 0:
    return False
  parentheses = []
  isValidParentheses = False
  for char in s:
      if char == '(':
        parentheses.append(')')
      elif char == '[':
        parentheses.append(']')
      elif char == '{':
        parentheses.append('}')
      else:
        if len(parentheses) > 0 and parentheses[-1] == char:
          del parentheses[-1]
        else:
          return False
  if parentheses == []:
    isValidParentheses = True
  return isValidParentheses
print(isValidParentheses('([()][]{})')) #)True
