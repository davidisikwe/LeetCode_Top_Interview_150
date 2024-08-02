class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums
        if len(nums) == 0:
            return nums
        a= 0
        z= -1
        while a < k:
            nums.insert(0, nums[z])
            nums.pop()
            a += 1
        return nums



#Time complexity- O(k * n)- O(n^2)
#Space complexity- O(1)
