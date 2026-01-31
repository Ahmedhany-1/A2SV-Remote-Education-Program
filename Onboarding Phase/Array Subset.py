from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
         countA = Counter(a)
         countB = Counter(b)

         for x in countB:
             if countB[x] > countA[x]:
                 return False
    