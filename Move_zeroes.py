class Solution(object):
    def moveZeroes(self, nums):
        c=nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for i in range(c):
            nums.append(0)
                
