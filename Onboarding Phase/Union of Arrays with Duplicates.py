class Solution:    
    def findUnion(self, a, b):
        ans = set()
        
        for i in a:
            ans.add(i)
        for i in b:
            ans.add(i)
            
        return list(ans)
        