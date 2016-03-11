class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # extreme cases: single-len str OR numRows=1
        if len(s) <= numRows or numRows == 1:
            return s
        
        # 5 rows:
        # =======
        # 0    8        16
        # 1   79      15
        # 2  6 10   14  
        # 3 5  11 13
        # 4    12
        ss = ''
        for row in range(numRows):
            # start pos = row#
            pos = row
            
            while pos < len(s):
                ss = ss + s[pos]
            
                # if not 1st or last row, add middle
                if row != 0 and row != numRows-1:
                    mid_pos = pos + (numRows-row-1)*2
                    if mid_pos < len(s): 
                        ss = ss + s[mid_pos]
            
                pos += numRows*2 - 2 
        return ss

print Solution().convert('abcdefghijkl', 3)
