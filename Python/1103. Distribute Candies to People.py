class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        temp = 0
        n = 1
        while candies > 0:
            if candies < n:
                result[temp] += candies
                break
            else:
                result[temp] += n
            candies -= n
            if temp >= num_people - 1:
                temp = 0
            else:
                temp += 1
            n += 1
        return result
