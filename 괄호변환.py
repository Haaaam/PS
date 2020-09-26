#균형잡힌 문자열인지 확인
def balance(p):
    cnt=0
    for i in range(len(p)):
        if p[i]=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            return i
#올바른 문자열인지 확인        
def proper(p):
    cnt=0
    for i in p:
        if i=='(':
            cnt+=1
        else:
            if cnt==0:
                return False
            cnt-=1
    return True

def solution(p):
   
    answer=""
    #1 입력이 빈 문자열일 경우, 빈 문자열을 반환
    if p==""
        return answer
    #2 문자열 p를 두 "균형잡힌 괄호 문자열"u,v로 분리     
    index=balance(p)
    u=p[:index+1]
    v=p[index+1:]
    
    #3-1수행
    if proper(u):
        answer=u+solution(v)
    
    #4 u가 올바른 괄호 문자열이 아닐 경우
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
       answer=''.join(u)
    return answer
      

     
