class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print s
        # max len is 1 by default
        max_len = 1
        
        # p1 = start of substring, p2 = end of substring
        p1 = 0
        p2 = 1
        
        while p2 < len(s):
            # i = index of s[p2] in substring [p1:p2]
            i = s[p1:p2].find(s[p2])
            
            # i != -1, means hitting a repeating char
            if i != -1:
                # update max_len if bigger
                if (p2 - p1) > max_len:
                    max_len = p2 - p1

                # move p1, instead of +1
                p1 += i+1
                    
            p2 += 1

        if (p2 - p1) > max_len:
            return p2 - p1

        return max_len

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring('au')
    print Solution().lengthOfLongestSubstring('cdd')
    print Solution().lengthOfLongestSubstring('abcdd')
    print Solution().lengthOfLongestSubstring('abcdcghijklmd')
