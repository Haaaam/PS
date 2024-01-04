def solution(arr):
    stk=[]
    for i in range(len(arr)):
        if len(stk)==0:
            stk.append(arr[i])
        elif len(stk)!=0:
            if stk[-1]==arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
    if len(stk)==0:
        stk.append(-1)
    return stk

