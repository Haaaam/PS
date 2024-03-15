# 정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러개가 담긴 리스트 num_list가 주어진다.
# slicer에 담긴 정수를 차례대로 a,b,c,라고 할때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 한다.

def solution(n, slicer, num_list):

    if n==1:
        return num_list[:slicer[1]+1]
    elif n==2:
        return num_list[slicer[0]:]
    elif n==3:
        return num_list[slicer[0]:slicer[1]+1]
    elif n==4:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]

n=4
slicer=[1,5,2]
num_list=[1,2,3,4,5,6,7,8,9]
print(solution(n,slicer,num_list))