
# Problem: Range vowel count queries
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/range-vowel-count-queries/1
# Time Complexity: O(n)
# Space Complexity: O(n) as we use prefix array
# Approach: We simple store vowel count in prefix for o(1) look up and then run the range queries


from collections import defaultdict
class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        vowels = 0
        prefix = [0] * (len(s)+1)
        for i,ch in enumerate(s):
            if ch in ('a','e','i','o','u'):
                vowels+=1
            prefix[i+1] = vowels
        ans = []
        for q in queries:
            start,end = q
            ans.append(prefix[end+1]-prefix[start])
        return ans
            