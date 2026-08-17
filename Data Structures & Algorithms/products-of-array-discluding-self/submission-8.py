class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        total = 1
        ans = [0] * len(nums)

        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                total *= num

        if count_zero > 1:
            return ans

        if count_zero == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans[i] = total
            return ans

        for i in range(len(nums)):
            ans[i] = total // nums[i]

        return ans