# 다시 풀어볼 것
def solution(str1,str2):
    str1 = str1.upper()
    str2 = str2.upper()

    str1_ = [str1[i:i + 2] for i in range(len(str1) - 1)]
    str2_ = [str2[i:i + 2] for i in range(len(str2) - 1)]

    # 특수문자 빼기
    tmp = [i for i in str1_ if i.isalpha()]
    str1_ = tmp.copy()
    tmp = [i for i in str2_ if i.isalpha()]
    str2_ = tmp.copy()

    # 교집합
    intersection = []
    tmp = str2_.copy()
    for i in str1_:
        if i in tmp:
            tmp.remove(i)
            intersection.append(i)

    union = len(str1_) + len(str2_) - len(intersection)

    if len(str1_) == 0 and len(str2_) == 0:
        answer = 1
    else:
        answer = (len(intersection) / union)
    return int(answer*65536)

str1="handshake"
str2="shake hands"
str1=str1.upper()
str2=str2.upper()

str1_=[str1[i:i+2] for i in range(len(str1)-1)]
str2_=[str2[i:i+2] for i in range(len(str2)-1)]

# 특수문자 빼기
tmp=[i for i in str1_ if i.isalpha()]
str1_=tmp.copy()
tmp=[i for i in str2_ if i.isalpha()]
str2_=tmp.copy()

# 교집합
intersection=[]
tmp=str2_.copy()
for i in str1_:
    if i in tmp:
        tmp.remove(i)
        intersection.append(i)

union=len(str1_)+len(str2_)-len(intersection)



if len(str1_)==0 and len(str2_)==0:
    answer=1
else:
    answer=(len(intersection)/union)
print(int(answer*65536))