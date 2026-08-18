class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        maxi = -1
        n = len(nums)
        count = [0]*51 
        if n == k:
            return max(nums)
        for x in nums:
            count[x]+=1
        if k == 1:
            for i in range(50,-1,-1):
                if count[i] == 1:
                    return i 
            return -1 
        if count[nums[0]]==1:
            maxi=max(maxi,nums[0])
        
        if count[nums[-1]]==1:
            maxi=max(maxi,nums[-1])
        return maxi