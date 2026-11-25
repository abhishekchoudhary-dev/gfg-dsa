# Problem: Repeated pattern check
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/shortest-unique-prefix-for-every-word/repeated-pattern-check/1
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a stack
# Approach: We need to basically make groups with the maximum run and then loop over the groups 
# and check if its same as previous group and based on count just pop the stack. If at the end the stack is empty
# then that means that all groups are balanced

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
                