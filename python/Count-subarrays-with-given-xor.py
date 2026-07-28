# Problem: Count subarrays with given xor
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/count-subarrays-with-given-xor/1
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: We make a hashmap and keep a track of how many off numbers we have been and keep adding that to the hashmap
# the hasmap stores a prefix sum basically of how many odd numbers till curr_xor ^ k as xor of itself comes out to zero.
# then we add curr_xor value to the hashmap.

from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, m):
        # code here
        d = defaultdict(int)
        d[0]=1
        result = 0
        curr_xor = 0
        for num in arr:
            curr_xor ^= num
            result+=d[curr_xor^k]
            d[curr_xor]+=1
        return result