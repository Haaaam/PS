def camelcase(s):
    cnt=1
    for i in s:
        if i.isupper():
            cnt+=1
    return cnt
s=input()
print(camelcase(s))

