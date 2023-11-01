# 15번 팔씨름을 하여 8번 이상 이기는 사람이 점심 값을 면제받기로 하였다
# 길이가 k인 'o' 또는 'x'로만 구성된 문자열 S[1..k]로 나타낼 수 있다.
# S[i]가 'o'면 소정이가 i번째 경기에서 승리, 'x'면 패배
n=int(input())
for i in range(n):
    tmp=input()
    ans='YES'
    if len(tmp)<=15:
        if tmp.count('x')>=8:
            ans='NO'

    print(f"#{i+1} {ans}")