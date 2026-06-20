class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # best for time: use a set. o(n) time, o(n) space
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False