class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount, pCount, sL, pL = {}, {}, len(s), len(p)
        if sL < pL: return []

        for i in range(pL):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = []
        if pCount == sCount:
            res.append(0)
        
        # s = "ab[ab]", p = "ab"
        # s{a:1, b:2} p{a:1, b:1} 
        # res = [0, 1, ]
        left = 0
        for i in range(pL, sL):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

            lch = s[left]
            sCount[lch] -= 1
            left += 1
            
            if sCount[lch] == 0:
                sCount.pop(lch)
            if pCount == sCount:
                res.append(left)
            
        return res


        

