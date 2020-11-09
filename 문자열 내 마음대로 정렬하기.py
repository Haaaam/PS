def solution(strings,n):

    return sorted(strings,key=lambda strings:(strings[n],strings))
strings=input().split()
n=int(input())
print(solution(strings,n))