# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):  
  max_profit = 0
  min_price = 10001
  for price in prices:
    min_price = min(price, min_price)
    profit = price - min_price
    max_profit = max(max_profit, profit)
  return max_profit

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,2,15,1,10,4])) # 13
