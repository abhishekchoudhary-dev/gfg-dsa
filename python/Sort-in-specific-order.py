# Problem: Sort in specific order
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/sort-in-specific-order/1
# Time Complexity: O(n)
# Space Complexity: O(1) - forced by the question
# Approach: We need to see that its usual in place sorting so either we can use partitioning of the array and then swapping the individual parts of odd and even
# which will work in Java as in place sorting can take index etc but not in Python where slicing will make a new array
# hence we use the trick of negating the odd numbers so usual sort will make them oppositive in descending order.

class Solution:
    def sortIt(self, arr):
        # code here
        #space expected in O(1)
    
        for i in range(len(arr)):
            if arr[i]%2==1:
                arr[i] = -arr[i]
        arr.sort()
        for i in range(len(arr)):
            if arr[i]%2==1:
                arr[i] = -arr[i]
        
                    
