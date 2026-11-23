# Problem: Two pairs with same sum
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/two-pairs-with-same-sum/1
# Time Complexity: O(n^2)
# Space Complexity: O(n) as we use hashmap
# Approach: We basically save the sums seen in the hashmap and while making a nested loop a second time
# we look the pair sums in the hashmap and if we find it we compare it with out answer and update the answer
# if the quadrulpet found is smaller than the other one. We just need to chain our loop bounds as we dont want to include
# values which can never find a quadruplet.


class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        # code here
        # since distinct and lexico smaller
        # we must ensure a<c
        # rest doest no matter
        # i can store sums first
        sums = {}
        for i in range(len(arr)-3):
            for j in range(i+1,len(arr)):
                if (arr[i] + arr[j] not in sums):
                    sums[arr[i]+arr[j]] = [i,j]
        ans = [float('inf'),float('inf'),float('inf'),float('inf')]
        found = False
        for k in range(1,len(arr)-1):
            for l in range(k+1,len(arr)):
                if arr[k]+arr[l] in sums:
                    i,j = sums[arr[k]+arr[l]]
                    if i<k and k!=j and l!=j:
                        ans = min(ans,[i,j,k,l])
                        found = True
        if not found:
            return [-1,-1,-1,-1]
        return ans