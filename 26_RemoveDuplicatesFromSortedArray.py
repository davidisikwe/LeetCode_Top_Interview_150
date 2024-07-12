class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 0
        j= i+1
        k= 1
        if len(nums) == 0:
            return 0
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[k]= nums[j]
                i += 1
                k += 1
            j += 1
        return k

# Time complexity- O(n)
# Space complexity- O(1)
