class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        arr = []
        for char in s:
            arr.append(ord(char))
        
        for i in range(len(arr) - 1, 0, -1):
            sum+= abs(arr[i] - arr[i-1])
        
        return sum
