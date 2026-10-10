class Solution(object):
    def removeDuplicates(self, nums):
       a=sorted(set(nums))
       b=len(a)
       nums[:b]=a
       return b
