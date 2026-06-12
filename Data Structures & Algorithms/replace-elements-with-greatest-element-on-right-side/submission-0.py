class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # assume the first element is largest
        # check to its right, if > then left replace, else continue
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i+1:])  # max of everything to the right
        arr[-1] = -1
        return arr
