class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}
        k = len(p)

        # build p's frequency
        for ch in p:
            pCount[ch] = pCount.get(ch, 0) + 1

        # build the first window from s
        for ch in s[:k]:
            sCount[ch] = sCount.get(ch, 0) + 1

        res = []
        if sCount == pCount:
            res.append(0)

        l = 0
        # slide the window
        for r in range(k, len(s)):
            # add right char
            sCount[s[r]] = sCount.get(s[r], 0) + 1

            # remove left char
            left = s[l]
            sCount[left] -= 1
            if sCount[left] == 0:
                sCount.pop(left)
            l += 1

            if sCount == pCount:
                res.append(l)

        return res
