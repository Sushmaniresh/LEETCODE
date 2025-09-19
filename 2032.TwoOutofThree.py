class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = Counter()
        for n in nums1,nums2,nums3:
            freq.update(set(n))
        return [k for k,v in freq.items() if v >= 2]

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for i in set(nums1):
            if i in nums2 or i in nums3:
                ans.append(i)
        for i in set(nums2):
            if i in nums1 or i in nums3:
                if i not in ans:
                    ans.append(i)
        for i in set(nums3):
            if i in nums1 or i in nums2:
                if i not in ans:
                    ans.append(i)      
        return ans