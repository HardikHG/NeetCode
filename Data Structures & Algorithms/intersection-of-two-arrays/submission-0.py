class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=j=0
        a=[]
        nums1.sort()
        nums2.sort()
        while (i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                if nums1[i] not in a:
                    a.append(nums1[i])
                i+=1
                j+=1
        return a