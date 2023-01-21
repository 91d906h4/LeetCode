class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = ((100 - discount) / 100)
        self.customer = 1
        self.goods = {x: y for x, y in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        price = 0

        for p, a in zip(product, amount): price += self.goods[p] * a
        
        if self.customer % self.n == 0: price = price * self.discount
        
        self.customer += 1

        return price


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
