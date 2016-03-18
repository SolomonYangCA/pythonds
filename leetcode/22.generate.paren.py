class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def dfs(n, a, b, str):
            if a < n:
                dfs(n, a+1, b, str+'(')
            
            if b < a:
                dfs(n, a, b+1, str+')')

            if a == n and b == n:
                res.append(str)
        
        dfs(n, 1, 0, '(')
        
        return res

print '\n'.join(Solution().generateParenthesis(4))
