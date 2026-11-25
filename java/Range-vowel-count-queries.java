import java.util.*;

/* 
# Problem: Range vowel count queries
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/range-vowel-count-queries/1
# Time Complexity: O(n)
# Space Complexity: O(n) as we use prefix array
# Approach: We simple store vowel count in prefix for o(1) look up and then run the range queries
*/

class Solution {
    public ArrayList<Integer> countVowels(String s, int[][] queries) {
        // code here
        int [] prefix = new int[s.length()+1];
        Arrays.fill(prefix,0);
        int vowels = 0;
        String v = "aeiou";
        for(int i=0;i<s.length();i++){
            if (v.contains(String.valueOf(s.charAt(i)))) vowels+=1;
            prefix[i+1] = vowels;
        }
        ArrayList<Integer> ans = new ArrayList<>();
        for (int[] q: queries){
            int start = q[0],end=q[1];
            ans.add(prefix[end+1] - prefix[start]);
        }
        return ans;
    }
}
