# my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return
def solution(my_str, n):
    answer = []
    if len(my_str)%n!=0:

        for i in range(len(my_str)//n+1):
            answer.append(my_str[i*n:(i+1)*n])
    else:
        for i in range(len(my_str)//n):
            answer.append(my_str[i*n:(i+1)*n])
    return answer

my_str="abcdef123"
n=3
print(solution(my_str,n))