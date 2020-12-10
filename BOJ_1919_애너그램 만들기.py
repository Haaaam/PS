a=input()
b=input()
cnt=0
for i in range(97,123):
    cnt+=abs(a.count(chr(i))-b.count(chr(i)))
print(cnt)
