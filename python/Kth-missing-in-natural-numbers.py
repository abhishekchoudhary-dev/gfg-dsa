# Problem: kth missing in natural numbers
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/kth-missing-in-natural-numbers/1
# Time Complexity: O(n) - as we calculate prefix sum and then we go through the prefix sum array once to find the subarray with given sum.
# Space Complexity: O(1)
# Approach - We just run the loop and convert arr to set for fast look up. every time a natural number is not in s
# we decrement k. as soon as k reaches 0 we return the number as that is the kth number after the set has been either exhausted
# or there is a major gap in the elements.

class Solution:
    def findKthSmall(self, arr, k):
        # code here
        s = set(arr)
        for i in range(1,2**31):
            if i not in s:
                k-=1
                if k == 0:
                    return i