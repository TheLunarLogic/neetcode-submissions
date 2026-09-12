class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # optimized
        s = set()
        n = len(nums)

        for i in range(n):
            mp = set()
            for j in range(i+1 , n):
                k = -(nums[i]+nums[j])
                if k in mp:
                    s.add(tuple(sorted([nums[i], nums[j], k])))
                mp.add(nums[j])

        return list(s)
            


