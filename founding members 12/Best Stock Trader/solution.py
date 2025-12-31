def maxProfit(prices: List[int]) -> int:

    max_profit = 0
    buy = 0

    for price in prices:
        if price < buy:
            buy = price
        else:
            profit = price - buy
            max_profit = profit

    return max_profit