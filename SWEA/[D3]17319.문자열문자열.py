tc=int(input())
for i in range(tc):
    n=int(input())
    s=input()
    res="No"
    if s[:len(s)//2]==s[len(s)//2:]:
        res="Yes"
    else:
        res="No"

    print(f"#{i+1} {res}")
