class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1: return "Flush"
        elif Counter(ranks).most_common()[0][1] >= 3: return "Three of a Kind"
        elif Counter(ranks).most_common()[0][1] == 2: return "Pair"
        else: return "High Card"
