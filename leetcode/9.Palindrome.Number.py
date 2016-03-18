class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # negative is False
        if x < 0:
            return False

        # 0-9, True:
        if x < 10:
            return True

        # ending with 0, False
        if x % 10 == 0:
            return False

        # get # digits of x and reversed x -> xx
        num_digits = 0
        xx = 0
        y = x
        while y > 0:
            xx = xx*10 + y%10
            num_digits += 1
            y = y/10

        print xx, num_digits
        # get left part of number
        l = x//(10**((num_digits + 1)//2))
        r = xx//(10**((num_digits + 1)//2))

        return  l == r

print Solution().isPalindrome(1000030001)
