class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        temp = []
        for i, j in enumerate(s):
            if goal[i] != j:
                temp.append(i)
        if len(temp) > 2: return False
        elif len(temp) == 2:
            goal = list(goal)
            goal[temp[0]], goal[temp[1]] = goal[temp[1]], goal[temp[0]]
            goal = "".join(goal)
            return s == goal
        else:
            if s == goal:
                return max(Counter(s).values()) >= 2
            else:
                return False
