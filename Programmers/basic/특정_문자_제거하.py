def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i == letter:
            continue
        else:
            answer += i
    return answer
# return my_string.replace(letter,'') # 다른 풀이

my_string='abcdef'
letter='f'
print(my_string.replace(letter,''))
answer=''
for i in my_string:
    if i==letter:
        continue
    else:
        answer+=i
print(answer)
