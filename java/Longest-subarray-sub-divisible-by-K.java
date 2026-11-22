import java.util.*;
/* 
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
*/

class Solution {
    public int longestSubarrayDivK(int[] arr, int k) {
        // code here
        int mx = 0;
        int currSum = 0;
        Map<Integer,Integer> map = new HashMap<>();
        map.put(0,-1);
        for (int i=0;i<arr.length;i++){
            currSum+=arr[i];
            int rem = (int)((currSum%k)+k)%k;
            if (map.containsKey(rem)){
                mx = Math.max(mx,i-map.get(rem));
            }
            else{
                map.put(rem,i);
            }
        }
        return mx;
    }
}