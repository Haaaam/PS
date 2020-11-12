def solution(x):
    result=0
    for i in str(x):
        result+=int(i)
    if x%result==0:
        return True
    else:
        return False
x=int(input())
print(solution(x))