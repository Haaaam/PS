# 주식 하나를 산다
# 원하는 만큼 가지고 있는 주식을 판다
# 아무것도 안한다
t=int(input())

for _ in range(t):

    n=int(input())
    arr=list(map(int,input().split()))
    buy=[]
    ans=0
    arr_max=max(arr)
    for j in range(n):
        if arr[j]!=arr_max:
            buy.append(arr[j])
        else:
            for i in range(len(buy)):
                ans+=arr_max-buy[i]
            buy=[]
            if arr_max!=arr[-1]:
                arr_max=max(arr[j+1:])
    print(ans)






