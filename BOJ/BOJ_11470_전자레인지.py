temp=[]
time=0
for i in range(5):
    temp.append(int(input()))
if temp[0]<0:
    time+=abs(temp[0])*temp[2]
    temp[0]=0
if temp[0]==0:
    time+=temp[3]
if temp[0]>=0:
    time+=(temp[1]-temp[0])*temp[4]
print(time)


