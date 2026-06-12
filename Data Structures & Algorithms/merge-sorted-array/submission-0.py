class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # nums1 total length. = m + n
        # first m elements is the values to be merged
        # n elements set to 0

        # merge the two arrays st final nums1 array is also sorted in
        # increasing order

        nums1[m:] = nums2
        nums1.sort()
