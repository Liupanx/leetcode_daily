from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if k > n: 
            return []

        pCount = Counter(p)
        sCount = Counter(s[:k])

        res = []
        if sCount == pCount:
            res.append(0)

        for i in range(n - k):
            left = s[i]
            right = s[i + k]

            sCount[left] -= 1
            if sCount[left] == 0:
                del sCount[left]

            sCount[right] = sCount.get(right, 0) + 1

            if sCount == pCount:
                res.append(i + 1)

        return res
