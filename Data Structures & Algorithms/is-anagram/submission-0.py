class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S_result = "".join(sorted(s))
        T_result = "".join(sorted(t))

        if S_result == T_result:
            return True
        return False
        