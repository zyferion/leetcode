# Problem 122
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

# Total profit = sum of only positive profits

def maxProfit(prices):
    
    # Initialise profit    
    total_profits = 0
    
    for i in range(1,len(prices)):
        
        profit = prices[i] - prices[i-1]
        
        print(f'Day: {i}')
        print(profit)
        
        if (profit > 0):
            
            total_profits += profit
            
    return (total_profits)
