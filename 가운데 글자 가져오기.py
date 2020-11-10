def solution(s):
    length=len(s)//2-1
    if len(s)%2==0:
        answer=s[length:length+2]
    else:
        answer=s[length+1]
    return answer

s=input()
print(solution(s))