#2021.02.25
#[BOJ]2437. 저울

n=int(input())
array=sorted(list(map(int,input().split())))
res=1
for i in array:
    if i<=res:
        res+=i
    else:
        break
print(res)

