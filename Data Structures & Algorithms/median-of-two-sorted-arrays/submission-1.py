class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        MergedList = []

        i = 0 
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                MergedList.append(nums1[i])
                i = i+1
            else:
                MergedList.append(nums2[j])
                j = j + 1
            
        MergedList.extend(nums1[i:])
        MergedList.extend(nums2[j:])

        n = len(MergedList)

        if n%2 == 1:
            return float(MergedList[n//2])
        return (MergedList[n // 2 - 1] + MergedList[n // 2]) / 2.0
        