# Problem: Any duplicates within k distance
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/any-duplicates-within-k-distance/1
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a hashmap
# Approach: We keep the numbers seen in a hashmap and keep adding their indices to a list. Before adding if 
# the number has been seen before meaning its values list is not empty and and the last occurence is <= k we immediately return true
# if its not then we return False

from collections import defaultdict
class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        # code here
        d = defaultdict(list)
        for i,num in enumerate(arr):
            if d[num] and i- d[num][-1] <= k:
                return True
            d[num].append(i)
        return False