class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 0
        j= i+ 2
        k= 2
        if len(nums) == 0:
            return 0
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[k] = nums[j]
                k += 1
                i += 1
            j += 1
        return k


# Time complexity- O(n)
# Space complexity- O(1)
