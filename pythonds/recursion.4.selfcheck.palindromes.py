import re

def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

for s in """
s
radar
hello
hannah
madam i'm adam
kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami;I'm a lasagna hog.
Able was I ere I saw Elba
Kanakanak
Wassamassaw""".split('\n'):
    s = re.sub("\.|'| |;|,", '', s.strip().lower())
    print isPalindrome(s), ' ', s

