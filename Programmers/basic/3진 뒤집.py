def solution(n):

    rev_base=''
    while n>0:
        n,mod=divmod(n,3) #divmod: 나눗셈
        rev_base+=str(mod)

    return int(rev_base,3)

# 3진법 상에서 앞되로 뒤집은 후, 이를 다시 10진법으로 표현
n=45
# result = 7
print(solution(n))
