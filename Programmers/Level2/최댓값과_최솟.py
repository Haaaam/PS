def solution(s):
    res = ''
    # arr=[int(i) for i in s.split()]
    arr = list(map(int, s.split()))
    res += str(min(arr)) + " "

    res += str(max(arr))

    return res

s="-1 -2 -3 -4"
print(solution(s))