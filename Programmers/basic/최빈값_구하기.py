def solution(array):
    dict={}
    for i in array:

        if str(i) not in dict:
            dict[str(i)]=1
        else:
            dict[str(i)]+=1



    a=[k for k,v in dict.items() if max(dict.values())==v]
    if len(a)==1:
        return int(a[0])
    else:
        return -1



array=[1,2,3,3,3,4]

dict={}
for i in array:

    if str(i) not in dict:
        dict[str(i)]=1
    else:
        dict[str(i)]+=1



a=[k for k,v in dict.items() if max(dict.values())==v]
if len(a)==1:
    print(int(a[0]))
else:
    print(-1)
