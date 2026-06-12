class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string s, if palindrome true else false
        # string is same forward and backward


        i, j = 0, len(s) - 1

        while i < j:
            # skip non-alphanumeric from left
            while i < j and not s[i].isalnum():
                i += 1
            
            # skip non-alphanumeric from right
            while i < j and not s[j].isalnum():
                j -= 1
            
            # compare (case-insensitive)
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True