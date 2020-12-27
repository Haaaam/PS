date=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(int(input())):
    t=input()
    month=int(t[4:6])
    day=int(t[6:])
    res="-1"
    if month>=1 and month<=12 and day>=1 and day<=date[month-1]:
        res=t[0:4]+"/"+t[4:6]+"/"+t[6:]
    print(f"#{i+1} {res}")
