# before의 순서를 바꿔서 after로 만들 수 있는가?

def solution(before,after):

    b={}
    a={}
    for i in before:
        b[i]=before.count(i)
    for j in after:
        a[j]=after.count(j)

    if b==a:
        return 1
    else:
        return 0

before="olleh"
after="hello"
print(solution(before,after))
