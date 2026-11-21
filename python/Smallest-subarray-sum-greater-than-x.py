
# Problem: Smallest subarray sum greater than x
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/smallest-subarray-sum-greater-than-x/1
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We need to find the smallest subarray so we take prefix sum
# and then we take deque where we store the indices of prefix sum and the moment the prefix sum of the subarray is greater than x for the current index
# we takes its distance from the initial index and we pop from the left of the queue and we keep popping till we can keep the sum > x
# as this will help us achieve the smallest subarray
# then we also do a pop loop in case of negative values seen because then prefix[i] becomes smaller than prefix[q[-1]]
# and then our while loop will never pop even when a smaller subarray is possible. So we have to keep the monotonic condition alive
# and hence we need to move past that index.


from collections import deque
class Solution:
    def smallestSubWithSum(self, arr, x):
        mn = float('inf')
        # code here 
        prefix_sum = [0]*(len(arr)+1)
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum+=arr[i] #maybe we can avoid this varibale totally
            prefix_sum[i+1] = curr_sum 

        q = deque()
        for idx, cur_sum in enumerate(prefix_sum):
            while q and cur_sum - prefix_sum[q[0]] > x:
                mn = min(mn, idx-q[0])
                q.popleft()
            while q and prefix_sum[q[-1]] >= cur_sum:
                q.pop()
            
            q.append(idx)
        return 0 if mn==float('inf') else mn