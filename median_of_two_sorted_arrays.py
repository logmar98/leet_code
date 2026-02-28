class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        size = len(nums)
        if size % 2 == 0:
            mid = nums[(size // 2) - 1] + nums[size // 2]
            return  mid / 2.0
        else:
            return float(nums[size // 2])
