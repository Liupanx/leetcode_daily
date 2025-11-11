class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_dict, p_dict, sL, pL = {}, {}, len(s), len(p)
        if sL < pL: return []
        res = []
        for i in range(pL):
            p_dict[p[i]] = 1 +  p_dict.get(p[i], 0)
            s_dict[s[i]] = 1 +  s_dict.get(s[i], 0)
        if s_dict == p_dict: res.append(0)

        l_pt = 0
        for i in range(pL, sL):
            remove = s[l_pt] #a
            l_pt += 1
            s_dict[s[i]] = 1 +  s_dict.get(s[i], 0) # a:2
            s_dict[remove] -= 1
            if s_dict[remove] == 0:
                s_dict.pop(remove)
            if s_dict == p_dict: 
                res.append(l_pt)

        return res