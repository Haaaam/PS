#2021.02.24
#[BOJ]11656. 접미사

s=input()
res=[]
tmp=''
for i in reversed(s):
    tmp+=i
    res.append(tmp[::-1])

for i in sorted(res):
    print(i)