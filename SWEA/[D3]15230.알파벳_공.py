tc=int(input())
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(tc):
    s=input()
    cnt=0
    for a,b in zip(s,alphabet):
        if a==b:
            cnt+=1
        else:
            break

    print(f"#{i+1} {cnt}")