# 38. Count and Say
def countAndSay(n):
  result = []
  sequence = [1]
  while n > 1:
    result = []
    currNum = sequence[0]
    k = 0
    for num in sequence:
      if num == currNum:
        k += 1
      else:
        result.append(k)
        result.append(currNum)
        k = 1
        currNum = num    
    result.append(k)
    result.append(currNum)
    sequence = result
    n -= 1
  result = ''.join(str(e) for e in sequence)
  return result

print(countAndSay(1)) # 1
print(countAndSay(2)) # 11
print(countAndSay(3)) # 21
print(countAndSay(4)) # 1211
print(countAndSay(5)) # 111221
print(countAndSay(6)) # 312211
print(countAndSay(7)) # 13112221
print(countAndSay(8)) # 1113213211
print(countAndSay(9)) # 31131211131221
print(countAndSay(10)) # 13211311123113112211
