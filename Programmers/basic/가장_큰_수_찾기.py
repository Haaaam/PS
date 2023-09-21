def solution(array):
    answer=[]
    a=max(array)
    return [a,array.index(a)]

array=[1,8,3]
res=[]
a=max(array)
print(a,array.index(a))