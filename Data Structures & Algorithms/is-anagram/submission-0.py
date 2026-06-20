class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. hashmap with counts of characters. 2. sorting
        return sorted(s) == sorted(t)