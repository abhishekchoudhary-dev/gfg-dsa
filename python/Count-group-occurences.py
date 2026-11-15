# Problem: Count group occurrences
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/Easy/1
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Simple idea where we make runs and then we enter them in hashmap to keep a count.
# we can also direcly count the runs in the hashmap by keeping a previous pointer
# then the group freq of the character is equal to k then we return it
 
from collections import defaultdict
class Solution:
    def getCount (self, s, k):
        # code here
        groups = []
        for char in s:
            if groups and char==groups[-1][0]:
                groups[-1][1]+=1
            else:
                groups.append([char,1])
        
        d = defaultdict(int)
        for group in groups:
            d[group[0]]+=1
        cnt = 0
        
        for key,value in d.items():
            if value==k:
                cnt+=1
        return cnt
        