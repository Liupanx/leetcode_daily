class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        for i in strs[1:]:
            while i.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
                

        # max_len = max(len(w) for w in strs)

        # matrix = [list(w.ljust(max_len, "_")) for w in strs]
        # for row in matrix:
        #     print(row)
        # prefix = ""
        # for col in range(max_len):
        #     chars = [row[col] for row in matrix]
        #     if len(set(chars)) == 1 and "_" not in chars:
        #         prefix += chars[0]
        #     else:
        #         break
        # return prefix