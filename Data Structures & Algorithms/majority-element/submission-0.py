class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # array nums with size n 
        # return element that appears > n/2, always exists

        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count +=1
            else:
                count -= 1
        return res

        
            
            
            
            
        