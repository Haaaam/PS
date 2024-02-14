# strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶기
# return: 가장 개수가 많은 그룹의 크기
def solution(strArr):
    """
    # dict 형식으로 푼 것
    strArr_length={}
    for i in strArr:
        if len(i) not in strArr_length:
            strArr_length[len(i)]=1
        else:
            strArr_length[len(i)]+=1

    return max(strArr_length.values())
    """
    strArr_length=[0]*len(strArr)
    for i in strArr:
        strArr_length[len(i)]+=1
    return max(strArr_length)
strArr=["a","bc","d","efg","hi"]
print(solution(strArr))