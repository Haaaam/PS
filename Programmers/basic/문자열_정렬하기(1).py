def solution(my_string):
    res=[]
    for i in my_string:
        try:
            res.append(int(i))
        except:
            pass

    return sorted(res)

my_string="hi12392"
print(solution(my_string))
