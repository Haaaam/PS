def appendAndDelete(s,t,k):
    s_len=len(s)
    t_len=len(t)
    if s_len+t_len<=k:
        return "Yes"
    s_cnt=0
    for ss,tt in zip(s,t):
        if ss==tt:s_cnt+=1
        else:break
    diff=s_len-s_cnt+t_len-s_cnt
    # 두 문자열 간의 차이가 홀수인지 확인. 이 경우 문자열을 동일하게 만들기 위해 짝수 추가/삭제 작업을 수행할 수 있다.
    if diff<=k and diff%2==k%2:
        return "Yes"
    else:
        return "No"



s=input()
t=input()
k=int(input())
print(appendAndDelete(s,t,k))