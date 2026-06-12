class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set, if something is in set and we go over again, return true

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
                
        
