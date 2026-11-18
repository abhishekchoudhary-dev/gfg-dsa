/* 
# Problem: XOR of number range
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/xor-of-number-range/1
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We need to understand that the xor of 4 consecutive numbers from multiple of 4 is zero
# so accordingly we need to take the start and end elements as multiple of 4 and calculate their gap from l and r
# and only take these numbers in our calculation.
*/

class Solution {
    public int findXOR(int l, int r) {
        // code here
        int start = (l/4)*4;
        int end = (r/4)*4;
        int xor = 0;
        for (int i=start;i<l;i++){
            xor^=i;
        }
        for (int i=end;i< r+1 ; i++){
            xor^=i;
        }
        return xor;
    }
}