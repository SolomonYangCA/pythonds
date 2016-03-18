class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh = len(haystack)
        ln = len(needle)
        
        if lh == 0 or ln == 0:
            return -1
            
        if ln > lh:
            return -1
            
        # lp, list of potenial pos
        lp = range(lh - ln + 1)

        for i in range(len(needle)):
            tmpl = []
            print lp
            for j in lp:
                if j+ln-i >= lh:
                    break

                if haystack[j+i] == needle[i]:
                    tmpl.append(j)
            
            if len(tmpl) == 0:
                return -1

            lp = tmpl

        return lp[0]

#                        01234567890
print Solution().strStr("mississippi", "sipp")
