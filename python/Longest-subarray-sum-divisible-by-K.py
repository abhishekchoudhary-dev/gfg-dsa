
# Problem: Longest subarray sum divisible by K
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/longest-subarray-sum-divisible-by-k/1
# Time Complexity: O(n) as go over the array
# Space Complexity: O(n) as we enter values in hashmap
# Approach: We simply store the remainders of subarray sum in hashmap and if we have seen a remainder before
# then its means that the subarray between them is dvisible by K. However, in java and C++ we need to keep a check that 
# they use truncated division over floorDivision like python because truncated is faster for the CPU.
# So we need to convert it to positive remainder for hashmap to store correct values. If a value exists we dont overwrite it 
# becasue we need the longest subrray. and if it exists we take the length between the current index and the index saved in hashmap
# and that is the longest subarray


class Solution:
    def longestSubarrayDivK(self, arr, k):
        # code here
        mx = 0
        d = {0:-1}
        curr_sum = 0
        for i,num in enumerate(arr):
            curr_sum+=num
            if curr_sum%k in d:
                mx = max(mx,i- d[curr_sum%k])
            else:
                d[curr_sum%k] = i
        return mx