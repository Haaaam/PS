arr=[1,1,1,0]
k=4
arr_s=[]

answer=[]
for i in arr:
    if i not in arr_s:
        arr_s.append(i)

if len(arr_s)>=k:
    answer=arr_s[:k]

else:
    answer=arr_s
    if len(answer)<k:
        for i in range(k-len(answer)):
            answer.append(-1)
print(answer)