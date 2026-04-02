class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            start=nums2.index(i)
            found=False
            for j in range(start+1,len(nums2)):
                if nums2[j]>i:
                    ans.append(nums2[j])
                    found=True
                    break
            if not found:
                ans.append(-1)
        return ans