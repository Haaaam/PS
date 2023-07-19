def solution(s):

    s=s.lower()
    if s.count("p")==s.count("y"):
        return True
    else:
        return False

s="Pyy"
print(s.lower())
print(solution(s))