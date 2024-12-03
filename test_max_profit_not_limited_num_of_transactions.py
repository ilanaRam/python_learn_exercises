
def max_profit_2(prices):
    profit = 0

    for i in range(1, len(prices)): # range give iterable from 0 (or from what defined) till len-1
        if prices[i] > prices[i - 1]: # else we will get negative profit which isnt good
            # sum + = next - prev
            profit += prices[i] - prices[i - 1]
    return profit
    # (5-1)+(6-3) = 7



# Driver Code
if __name__ == '__main__':
    # Stock prices on consecutive days
    prices = [7, 1, 5, 3, 6, 4]

    profit = max_profit_2(prices)
    print(profit)