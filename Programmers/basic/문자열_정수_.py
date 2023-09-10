def solution(num_str):


    return sum(int(i) for i in num_str if i!="0")

num_str=input()
num_str=list(num_str)
answer=sum(int(i) for i in num_str if i!=0)
print(answer)