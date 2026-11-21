import java.util.*;
/* 
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
*/

class Solution {
    public int smallestSubWithSum(int[] arr, int x) {
        // code here
        int[] prefix = new int[arr.length+1];
        int mn = Integer.MAX_VALUE;
        Arrays.fill(prefix,0);
        for (int i=0;i<arr.length;i++){
            prefix[i+1] = prefix[i] + arr[i];
        }
        Deque<Integer> d = new ArrayDeque<>();
        
        for(int i = 0; i< prefix.length;i++){
            while (!d.isEmpty() && (prefix[i] - prefix[d.getFirst()] > x) ){
                mn = Math.min(mn, i - d.getFirst());
                d.removeFirst();
                
            }
            
            while (!d.isEmpty() && (prefix[d.getLast()] >= prefix[i])){
                d.removeLast();
            }
            //second loop is required or it cannot get shorter

            d.addLast(i);
        }
        if (mn==Integer.MAX_VALUE) return 0;
        return mn;
    }
}