class Solution(object):
    def maxProduct(self, nums):
        res=max(nums)
        currMin, currMax= 1,1
        for n in nums:
            temp=n*currMax
            currMax=max(n*currMax,n*currMin,n)
            currMin=min(temp,n*currMin,n)
            res=max(res,currMax)
        return res
        