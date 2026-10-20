class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # Agar koi nayi choti price milti hai toh use update kar lo
            if price < min_price:
                min_price = price
            else:
                # Agar aaj beche toh kitna profit hoga calculate karo
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
                    
        return max_profit