class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sn = sorted(nums)
        res = []
        
        a, b = 0, len(sn)-1
        
        counter = 0
        while b-a > 2:
            x = a+1
            y = b-1

            while x < y:
                sum = sn[a]+sn[x]+sn[y]+sn[b]

                if sum == target and (sn[a],sn[x],sn[y],sn[b]) not in res:
                    res.append([sn[a],sn[x],sn[y],sn[b]])
                    x = x+1
                    y = y-1
                elif sum < target:
                    x = x+1
                else:
                    y = y-1
            
            counter += 1
            if counter % 2:
                a += 1
            else:
                b -= 1
        
        return res

print Solution().fourSum([0,0,0,0], 0)
