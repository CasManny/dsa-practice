def best_time_to_buy_stock(prices):
    max_profit = 0
    left, right = 0, 1
    while right  <  len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit

prices = [7,1,5,3,6,4]
print(best_time_to_buy_stock(prices))
        