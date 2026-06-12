class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # array nums with size n 
        # return element that appears > n/2, always exists

        threshold = len(nums) / 2

        seen = {}
        for num in nums:
            if num in seen:
                seen[num] +=1
            
            else:
                seen[num] = 1

            if seen[num] > threshold:
                return num


                
        
            
            
            
            
        