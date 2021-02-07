'''n,m,k=map(int,input().split())
max_lst=[n,m,k]
if n==m==k:
    print(10000+n*1000)
elif n==m or m==k:
    print(1000+m*100)
elif n==k:
    print(1000+k*100)
elif n!=m and m!=k and k!=n:
    print(max(max_lst)*100)'''

max_lst=sorted(list(map(int,input().split())))

if len(set(max_lst))==1:
    print(10000+max_lst[0]*1000)
elif len(set(max_lst))==2:
    print(1000+max_lst[1]*100)
else:
    print(max_lst[2]*100)





