import sys 
from typing import List
# sys.maxsize & -sys.maxsize를 통해 최대 최소값 설정 가능

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                continue
            profit = max(prices[i] - prices[buy], profit)
        return profit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize 
        profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = max(price - min_price, profit)

        return profit
