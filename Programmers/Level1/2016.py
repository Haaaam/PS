def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return date[(sum(month[:a - 1]) + b - 1) % 7]
a,b=map(int,input().split())
print(solution(a,b))
