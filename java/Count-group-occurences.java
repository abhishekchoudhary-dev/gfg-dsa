/* 
# Problem: Count group occurrences
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/Easy/1
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Simple idea where we make runs and then we enter them in hashmap to keep a count.
# we can also direcly count the runs in the hashmap by keeping a previous pointer
# then the group freq of the character is equal to k then we return it
*/

import java.util.*;
class Solution {
    int getCount(String s, int k) {
        // code here
        List<List<Object>> groups = new ArrayList<>();
        for (char ch: s.toCharArray()){
            if (!groups.isEmpty() && ch == (char) groups.get(groups.size()-1).get(0)){
                List<Object> last = groups.get(groups.size()-1);
                last.set(1,(int)last.get(1)+1);
            }
            else {groups.add(new ArrayList<>(List.of(ch,1)));}
        }
        int cnt = 0;
        Map<Character,Integer> map = new HashMap<>();
        for(List<Object> group : groups){
            char key = (char) group.get(0);
            map.put(key, map.getOrDefault(key,0) + 1);
        }
        for(Map.Entry<Character,Integer> entry: map.entrySet()){
            if (entry.getValue() == k) cnt++;
        }
        return cnt;
    }   
}
