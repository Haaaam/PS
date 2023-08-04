def solution(strings,n):

    return sorted(strings,key=lambda strings:(strings[n],strings))
strings=["sun", "bed", "car"]
n=1
print(solution(strings,n))


