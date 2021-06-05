import sys

class Solution:
    def __init__(self):
        self.
    def pushCharacter(self,char):
    def enqueueCharacter(self,char):
    def popCharacter(self,):
    def dequeueCharacter(self):

s=input()
obj=Solution()
l=len(s)
for i in range(len(l)):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True

for i in range(l//2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")


