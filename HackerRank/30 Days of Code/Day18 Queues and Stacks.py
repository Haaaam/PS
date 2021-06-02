import sys

class Solution:

s=input()
obj=Solution()
l=len(s)
for i in range(len(l)):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True


