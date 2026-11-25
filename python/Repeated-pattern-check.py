# Problem: Repeated pattern check
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/shortest-unique-prefix-for-every-word/minimum-jumps/1
# Time Complexity: O(nxL) - where we have n strings and L is the avg length
# Space Complexity: O(nxL)
# Approach: We make a trie and instead of trie just giving prefix added a counter to each node 
# to see how many strings pass through it. then we only take the nodes where the count is 1


class Solution:
    def findPattern(self, s):
        # code here
        groups = []
        for ch in s:
            if groups and groups[-1][0] == ch:
                groups[-1][1]+=1
            else:
                groups.append([ch,1])
        stack = []
        
        for group in groups:
            if group[0]=='y':
                if not stack or stack[-1][0]!='x' or stack[-1][1]!=group[1]:
                    return False
                stack.pop()
            else:
                stack.append(group)
        return len(stack)==0
                