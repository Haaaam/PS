t=int(input())

for i in range(t):
    s=input()
    tmp=[]
    for idx in range(1,len(s)):
        tmp.append(int(s[:idx])+int(s[idx:]))
    print(f"#{i+1} {min(tmp)}")

