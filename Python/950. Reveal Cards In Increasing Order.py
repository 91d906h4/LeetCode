class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        result = [deck.pop(0)]
        for i in deck:
            t = result.pop(0)
            result.append(t)
            result.append(i)
        return reversed(result)
