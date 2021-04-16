name_lst=[]
for i in range(int(input())):
    name,day,month,year=input().split()
    if len(month)==1:
        month='0'+month
    if len(day)==1:
        day='0'+day
    name_lst.append((name,int(year+month+day)))
name_lst.sort(key=lambda x:x[1])
print(name_lst[-1][0])
print(name_lst[0][0])

