def sumInts(arr1, arr2):
  #revence arrays that represent numbers
  num1 = arr1[::-1]
  num2 = arr2[::-1]
  # tracking digit transfer
  exceedsTen = False
  result = []

  # make arrays equal length 
  maxDigits = max(len(num1), len(num2))
  if len(num1) > len(num2):
    for i in range(len(num2), len(num1)):
      num2.append(0)
  if len(num2) > len(num1):
    for i in range(len(num1), len(num2)):
      num1.append(0)

  # sum two "numbers"
  for i in range(maxDigits):
    foo = num1[i] + num2[i]
    if exceedsTen:
      foo += 1
    if foo < 10:
      exceedsTen = False
      foo = foo
    if foo > 9:
      exceedsTen = True
      foo = foo % 10
    result.append(foo)

  # checking special condition
  # if last colculation exceed 10
  if exceedsTen:
    result.append(1)
  
  return result[::-1]

print(sumInts([1],[9]))      #[1,0]
print(sumInts([1],[9,9]))    #[1,0,0]
print(sumInts([1,1],[9,9]))  #[1,1,0]
print(sumInts([9,9,9],[1]))  #[1,0,0,0]
