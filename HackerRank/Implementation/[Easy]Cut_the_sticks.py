n=int(input())
arr=list(map(int,input().split()))
while len(arr)!=0:
    cut=min(arr)
    n_cut=0
    ans=[]
    for i in range(len(arr)):
        if arr[i]>=cut:
            arr[i]-=cut
            n_cut+=1
    print(n_cut)
    arr=list(filter(lambda x: x>0,arr))
