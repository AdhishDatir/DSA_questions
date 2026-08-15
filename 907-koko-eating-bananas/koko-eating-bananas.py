class Solution:
    #ad
    def helper(self,arr,hourly):
        hr = 0
        for i in range(len(arr)):
            hr += math.ceil( arr[i] / hourly )
        return hr 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        low = 1
        high = max(piles)

        while low <= high:
            mid =(low + high )//2
            if self.helper(piles,mid) <= h:
                high = mid -1 
            else:
                low = mid + 1
        return low
        