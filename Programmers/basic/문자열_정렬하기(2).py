def solution(my_string):
    answer=sorted(my_string.lower())

    return ''.join(answer)

my_string="Bcad"
print(solution(my_string))

