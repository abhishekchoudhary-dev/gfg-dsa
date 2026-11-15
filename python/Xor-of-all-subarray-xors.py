# Problem: xor of all subarray xors
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/xor-of-all-subarray-xors/1
# Time Complexity: O(n) - as we calculate the sum in advance 
# Space Complexity: O(1)
# Approach: If we use tradition technique then we can do the prefix sum of the xor 
# and then in the nested loop we do ^ of prefix[j+1] and prefix[i] to find the xor between the elements
# but that is TLE so we have to use the contirbution technique. That if the elemnts contibutes to even number of subarrays
# then ofcourse all xor will be 0. if Odd then it will be the element itself. So we just make this calculation
# and if the subarray contribution is odd we xor it into the total

class Solution:
    def subarrayXor(self, arr):
        # code here 
        prefix = [0]*(len(arr)+1)
        xor = 0
        for i in range(len(arr)):
            xor^=arr[i]
            prefix[i+1] = xor
        total_xor = 0
        #try contribution technique
        for i in range(len(arr)):
            subarrays = (i+1) * (len(arr)-i)
            if subarrays%2==1:
                total_xor^=arr[i]
        return total_xor
        '''
        TLE brute force
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                sub_xor = prefix[j+1] ^ prefix[i]
                total_xor ^= sub_xor
        return total_xor
        '''