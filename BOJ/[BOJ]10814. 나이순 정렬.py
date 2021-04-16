#2021.02.13
#[BOJ]10814. 나이순 정렬

data=[]
for i in range(int(input())):
    old,name=input().split()
    data.append((int(old),name))


data=sorted(data,key= lambda x:x[0])
for i in data:
    print(i[0],i[1])