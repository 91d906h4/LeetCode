class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money if sum(sorted(prices)[:2]) > money else money - sum(sorted(prices)[:2])
