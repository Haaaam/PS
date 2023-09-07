def solution(code):
    code = list(code)
    mode = 0
    answer = ''
    for i in range(len(code)):
        if mode == 0:
            if code[i] != "1" and i % 2 == 0:
                answer += code[i]
            elif code[i] == "1":

                mode = 1
                pass
        elif mode == 1:

            if code[i] != "1" and i % 2 != 0:
                answer += code[i]
            elif code[i] == "1":
                mode = 0
                pass
    return answer if answer != '' else 'EMPTY'

code="aaa"


print(solution(code))