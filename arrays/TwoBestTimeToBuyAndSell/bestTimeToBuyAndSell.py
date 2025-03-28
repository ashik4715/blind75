# Best time to buy and sell stock - Google interviews (Leet code 121)
# two pointer concept l,r, l=buy, r = sell 7 > 1 1 - 7 -6 if l is greater than r then move l to r and r to +1 index
# now check again l = 1, r=5, maxprofit=4 update max profit, r = 3 maxprofit = 2no update, r = 6 maxprofit=5 update, r=4 maxprofit=5 no update
# found maxprofit space complexity: O(1), time Complexity : O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))

        
    