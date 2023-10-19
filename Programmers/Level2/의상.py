def solution(clothes):
    answer = 1
    clothes_dic = dict()
    for i in clothes:
        a, b = i[0], i[1]
        if b not in clothes_dic.keys():
            clothes_dic[b] = 1
        else:
            clothes_dic[b] += 1

    for k, v in clothes_dic.items():
        answer *= (v + 1)
    return answer

# 코니는 각 종류별로 최대 1가지 의상만 착용 가능
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로
# 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산
# 코니는 하루에 최소 한 개 이상의 의상은 입는다.
# clothes의 각 행은 [의상의 이름, 의상의 종류]
# return 서로 다른 옷의 조합의 수
clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
#clothes=[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# 수학공식으로 접근
"""
옷 종류가 1개: a =>(a+1)-1
옷 종류가 2개: a+b+ab => a(b+1)+b => (a+1)(b+1)-1
옷 종류가 3개: a+b+c+ab+ac+bc+abc => (a+1)(b+1)(c+1)-1
.
.
.
=> 
"""
answer=1
clothes_dic=dict()
for i in clothes:
    a,b=i[0],i[1]
    if b not in clothes_dic.keys():
        clothes_dic[b]=1
    else:
        clothes_dic[b]+=1


for k,v in clothes_dic.items():
    answer*=(v+1)
print(answer-1)

