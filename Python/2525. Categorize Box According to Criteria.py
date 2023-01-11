class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9:
            if mass >= 100: return "Both"
            else: return "Bulky"
        else:
            if mass >= 100: return "Heavy"
            else: return "Neither"
