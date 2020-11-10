def solution(s):
    length=len(s)
    if length==4 or length==6:
        if s.isdecimal():
            return True
        else:
            return False
    else:
        return False

s=input()
print(solution(s))