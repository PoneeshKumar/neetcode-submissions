class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # given array of characters "s", reverse string, O(1) extra memory
        len_s = len(s) - 1
        
        i = 0

        while i <= len_s:
            temp = s[i]
            s[i] = s[len_s]
            s[len_s] = temp

            i += 1;
            len_s -= 1
        
        return s

        

        