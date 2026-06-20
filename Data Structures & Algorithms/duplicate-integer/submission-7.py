class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set, if something is in set and we go over again, return true

        seen = set(nums)
        if len(seen) == len(nums):
            return False
        return True
                
        
