class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. hashmap with counts of characters. 2. sorting
        freq_s = {}
        freq_t = defaultdict(int)
        # 1. build frequency maps
        for c in s:
            freq_s[c] = freq_s.get(c, 0) +1
        
        for c in t:
            freq_t[c] += 1

        # iterate over keys in s, compare with frequencies in t
        for c in freq_s.keys():
            freq_t[c] -= freq_s[c]
            if freq_t[c] != 0:
                return False
        
        for c in freq_t.keys():
            if freq_t[c] != 0:
                return False

        return True