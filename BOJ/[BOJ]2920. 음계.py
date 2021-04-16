#2021.02.13
#[BOJ]2920. 음계

n=list(map(int,input().split()))
n_ascending=sorted(n)
n_descending=sorted(n,reverse=True)
if n==n_ascending:
    print("ascending")
elif n==n_descending:
    print("descending")
else:
    print("mixed")
