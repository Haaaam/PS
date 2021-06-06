import sys

class Solution:
    def __init__(self):
        self.stack=[]
        self.queue=[]
    def pushCharacter(self,char):
        self.stack.append(char)
    def enqueueCharacter(self,char):
        self.stack.insert(0,char)
    def popCharacter(self,):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop()

s=input()
obj=Solution()
l=len(s)
for i in range(l):
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


