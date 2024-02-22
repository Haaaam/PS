# 2016년 1월1일은 금요일. 2016년 a월 b일은 무슨 요일인가?

def solution(a, b):
    answer = ''
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    return day[(sum(month[:a-1])+b)%len(day)-1]

a,b=5,24
print(solution(a,b))