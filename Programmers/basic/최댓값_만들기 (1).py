def solution(numbers):
    answer = 0
    num_sor=sorted(numbers,reverse=True)
    return num_sor[0]*num_sor[1]