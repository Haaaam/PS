def solution(today,terms,privacies):
    res = []
    dic = dict()
    today = [int(i) for i in today.split('.')]
    today_day = today[0] * 12 * 28 + today[1] * 28 + today[2]
    for i in range(0, len(terms)):
        dic[terms[i].split(' ')[0]] = int(terms[i].split(' ')[1])
    # day로 변환해서 풀기

    for i in range(len(privacies)):
        date, check = privacies[i].split(' ')
        yy, mm, dd = date.split('.')
        # 약관 날짜
        day = int(yy) * 12 * 28 + int(mm) * 28 + int(dd)

        if today_day >= day + dic[check] * 28:
            res.append(i + 1)

    return res


# 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 한다.
# 모든 달은 28일까지 있다고 가정

### day 합산으로 접근해서 풀이
today= "2019.12.09"
terms= ["A 12"]
privacies=  ["2018.12.10 A", "2010.10.10 A"]
res=[]
dic=dict()
today=[int(i) for i in today.split('.')]
today_day=today[0]*12*28+today[1]*28+today[2]
for i in range(0,len(terms)):
    dic[terms[i].split(' ')[0]]=int(terms[i].split(' ')[1])
# day로 변환해서 풀기

for i in range(len(privacies)):
    date,check=privacies[i].split(' ')
    yy,mm,dd=date.split('.')
    # 약관 날짜
    day=int(yy)*12*28+int(mm)*28+int(dd)
    print(today_day)
    print(day+dic[check]*28)
    if today_day>=day+dic[check]*28:
        res.append(i+1)
print(res)

# 테스트케이스 6~19 틀림
"""
# today를 지났으면 파기
dic=dict()
for i in range(0,len(terms)):
    dic[terms[i].split(' ')[0]]=int(terms[i].split(' ')[1])
print(dic)
today=[int(i) for i in today.split('.')]
print(today)
for i in range(len(privacies)):

    date,check=privacies[i].split(' ')
    yy,mm,dd=date.split('.')
    yy,mm,dd=int(yy),int(mm),int(dd)
    mm+=dic[check]
    print(mm)
    dd-=1
    if mm>12:
        yy+=1
        if mm%12==0:
            mm=12
        else:
            mm%=12
    if dd==0:
        mm-=1
        dd=28
        if mm>12:
            yy+=1
            mm%=12
    print(yy,mm,dd)
    if today[0]>yy:
        res.append(i+1)
    elif today[0]==yy:
        if today[1]>mm:
            res.append(i+1)
        elif today[1]==mm:
            if today[2]>dd:
                res.append(i+1)



print(res)
"""