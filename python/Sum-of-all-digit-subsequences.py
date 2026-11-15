# Problem: Sum of all digit subsequences
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/sum-of-all-digit-subsequences/1
# Time Complexity: O(n) - as we calculate the sum in advance 
# Space Complexity: O(n) as we use hashmaps to store the remaining sum at each index
# Approach: All non empty subsequences for an array with no duplicates is basically the same as 
# all the subsets of the array. But instead of calculating all the subsets and taking the sum which is too long we use
# the contribution technique where we see how many subsets an array contributes to. for subarrays
# formula is element*(i+1)*(n-i) but subseuqnece or subsets are different so the contribution of each element
# is basically the value * 2^(n-1) as total we have 2^n subsets and it will occur in exactly half of the subsets
# so total contiribution will be 2^n/2 which is 2^(n-1)


import math

class Solution:

    def subsequenceSum(self, s):
        """code here"""
        MOD = 10**9+7
        val = sum(int(d) for d in s) 
        return int(val* pow(2,len(s)-1,MOD)) % MOD