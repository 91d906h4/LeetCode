class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stones.append(stones.pop() - stones.pop())
            print(stones)
        return stones[0]
