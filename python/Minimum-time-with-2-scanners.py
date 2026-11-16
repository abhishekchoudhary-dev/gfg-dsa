class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here
        def feasible(mid):
            total = mid//s1 + mid//s2
            return total >= n
            

        lo = 0
        hi = (s1+s2)*n
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if feasible(mid):
                ans= mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans