#2021.02.28
#[BOJ]14719. 빗물

h,w=map(int,input().split())
height=list(map(int,input().split()))
rain=0

for i in range(1,w-1):
    left=max(height[:i])
    right=max(height[i+1:])
    if min(left,right)-height[i]>0:
        rain+=min(left,right)-height[i]

print(rain)




