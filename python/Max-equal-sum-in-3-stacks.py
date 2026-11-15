# Problem: Max equal sum in 3 stacks
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/find-maximum-equal-sum-of-three-stacks/1
# Time Complexity: O(n) - as we calculate the sum in advance 
# Space Complexity: O(n) as we use hashmaps to store the remaining sum at each index
# Approach: We take the sum already at the beginning and then each index we added the sum
# in the hashmap which becomes the sum of the remaining elements from the current index.
# once this is done for all three arrays we iterate over one of them and keep reducing the sum for each index
# and keep checking if this sum occurs in the other two hashmaps. As soon as this conditions is true we return the sum
# as its guaranteed to get only smaller as we traverse the array so this become a monotonic conditions
# and hence if a sum is in all subarrays thats the maximum sum we can have.


from collections import deque
class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        # code here
        total = 0
        d1,d2,d3= {},{},{}
        sum1,sum2,sum3 = sum(s1),sum(s2),sum(s3)
        for i,e in enumerate(s1):
            d1[sum1] = i
            sum1-=e
        for i,e in enumerate(s2):
            d2[sum2] = i
            sum2-=e
        for i,e in enumerate(s3):
            d3[sum3]=i
            sum3-=e
        # now usual loop
        #print(d1,d2,d3)
        total = sum(s1)
        for i,e in enumerate(s1):
            if total in d2 and total in d3:
                return total
            total-=e
        return 0
            