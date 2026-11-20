
# Problem: Min flips for alternate
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/min-flips-for-alternate/1
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We either start with 0 or start with 1 and calculate how many flips we would need in both
# cases and then we return the minimum of both.


class Solution:
    def minFlips(self, s):
        # Code here
        z_start = 0
        o_start = 0
        for i,ch in enumerate(s):
            if i%2==0:
                if ch=='0':
                    o_start+=1
                else:
                    z_start+=1
            else:
                if ch=='0':
                    z_start+=1
                else:
                    o_start+=1
        return min(z_start,o_start)
