1from collections import Counter
2from typing import List
3
4class Solution:
5    def commonChars(self, words: List[str]) -> List[str]:
6        common = Counter(words[0])
7        
8        for word in words[1:]:
9            common &= Counter(word)
10
11        return list(common.elements())
12