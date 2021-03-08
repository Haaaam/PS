#2021.03.09
#[BOJ]2386. 도비의 영어 공부
while True:
    s=input().lower()
    if s[0]=="#":
        break
    else:
        print(s[0],s[1:].count(s[0]))
