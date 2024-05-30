class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest = min(prices)
        prices.remove(smallest)
        next_smallest = min(prices)
        if money >= smallest+next_smallest:
            return (money-(smallest+next_smallest))
        else:
            return money