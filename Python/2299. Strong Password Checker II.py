class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False
        if len(set(password) & set("abcdefghijklmnopqrstuvwxyz")) == 0: return False
        if len(set(password) & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) == 0: return False
        if len(set(password) & set("0123456789")) == 0: return False
        if len(set(password) & set("!@#$%^&*()-+")) == 0: return False
        if len(findall(r"(.)\1{1,}", password)) != 0: return False
        return True
