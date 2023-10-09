# 비밀지도

def solution(n,arr1,arr2):
    answer = []
    for i in range(n):
        result = str(bin(arr1[i] | arr2[i])[2:])

        if n > len(result):
            result = ("0" * (n - len(result))) + result

        result = result.replace("1", "#")
        result = result.replace("0", " ")
        answer.append(result)
    return answer

n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
# 각 칸은 "공백" 또는 "벽("#") 두 종류로 이루어져 있다.
# 지도 1과 지도 2 있음
# 하나라도 벽이면 벽
answer=[]
for i in range(n):
    result=str(bin(arr1[i]|arr2[i])[2:])
    print(result)

    if n>len(result):
        result=("0"*(n-len(result)))+result

    result=result.replace("1","#")
    result=result.replace("0"," ")
    answer.append(result)
print(answer)