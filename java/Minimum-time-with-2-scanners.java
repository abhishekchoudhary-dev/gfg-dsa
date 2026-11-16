/* 
# Problem: Mainimum time with 2 scanners
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/minimum-time-with-2-scanners/1
# Time Complexity: O(log n ) as we use binary search
# Space Complexity: O(1)
# Approach: We simply search on the solution search using binary search as input is 10^6.
*/

class Solution {
    
    private boolean feasible(int mid, int a, int b, int req){
        int total = mid/a + mid/b;
        return total>=req;
    }
    public int minTime(int n, int s1, int s2) {
        // code here
        int lo = 0;
        int hi = (s1+s2) * n;
        int ans = 0;
        while (lo < hi){
            int mid = (lo+hi)/2;
            if(feasible(mid,s1,s2, n)){
                ans = mid;
                hi = mid;
            }
            else {
                lo = mid+1;
            }
        }
        return ans;
    }
} {
    
}
