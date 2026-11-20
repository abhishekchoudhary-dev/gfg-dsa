/* 
# Problem: Min flips for alternate
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/min-flips-for-alternate/1
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We either start with 0 or start with 1 and calculate how many flips we would need in both
# cases and then we return the minimum of both.
*/

class Solution {
    public int minFlips(String s) {
        // code here
        int zStart = 0;
        int oStart = 0;
        for (int i=0; i < s.length();i++){
            if (i%2==0){
                if(s.charAt(i) == '0'){
                    oStart+=1;
                }
                else zStart+=1;
                
            }
            else{
                if(s.charAt(i) == '0'){
                    zStart+=1;
                }
                else oStart+=1;
            }
        }
        return Math.min(zStart,oStart);
    }
} {
    
}
