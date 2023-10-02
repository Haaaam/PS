def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += (i * n)
    return answer
my_string="hello"
n=3
answer=''
for i in my_string:
    answer+=(i*n)

print(answer)