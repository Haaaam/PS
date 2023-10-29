n=int(input())
dic={"MON":1,"TUE":2,"WED":3,"THU":4,"FRI":5,"SAT":6,"SUN":7}
for i in range(n):
    s=input()
    if s=="SUN":
        print(f"#{i+1} {dic[s]}")
    else:
        print(f"#{i+1} {dic['SUN']-dic[s]}")
