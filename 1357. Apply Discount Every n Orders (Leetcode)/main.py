class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.count = 1
        self.n = n
        self.discount = discount / 100
        self.dictionary = {}
        for i in range(len(products)):
            self.dictionary[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        final_cost = 0
        for i in range(len(product)):
            cost = self.dictionary[product[i]]
            item_amount = cost * amount[i]
            final_cost += item_amount

        if self.count % self.n == 0:
            self.count += 1
            new_amount = (final_cost) - (final_cost * (self.discount))
            return new_amount
        else:
            self.count += 1
            return final_cost

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

