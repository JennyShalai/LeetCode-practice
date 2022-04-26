#Given a roman numeral, convert it to an integer.
#It is guaranteed that s is a valid roman numeral in the range [1, 3999]

def romanToInt(s: str) -> int:
  translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
  number = 0
  s = s.replace("IV", "IIII").replace("IX", "VIIII")
  s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
  s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
  for char in s:
    number += translations[char]
  return number

print(romanToInt("MCMXCIV")) #1994
