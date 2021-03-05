from itertools import combinations
l,c=map(int,input().split())
alpha=sorted(list(input().split()))
arr=list(combinations(alpha,l))
vowel=['a','e','i','o','u']
for i in arr:
    cnt=0
    for k in i:
        if k in vowel:
            cnt+=1
    if cnt>=1 and cnt<=l-2:
        print(''.join(i))

