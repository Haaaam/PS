def solution(s,skip,index):

    #alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
     #           "v", "w", "x", "y", "z"]
    answer = ''
    for i in s:
        a = ord(i)
        b = index
        while b > 0:
            a += 1
            if a > ord('z'):
                a = ord('a')
            if chr(a) in skip:
                b += 1

            b -= 1

        answer += chr(a)
    return answer
# 다른 사람의 풀이
"""
def solution(s,skip,index):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    answer=''
    for i in skip:
        alphabet.remove(i)
    
    for i in s:
        answer+=alphabet[(alphabet.index(i)+index)%len(alphabet)]
    return answer
"""
# 처음 시도 테스트 케이스만 맞고 실패
"""
    for i in s:
        cnt = 0
        dis = alphabet.index(i) + index
        for j in skip:

            if j in alphabet[alphabet.index(i):dis]:
                cnt += 1

        if (dis + cnt) >= len(alphabet):
            answer += alphabet[len(alphabet) - (dis + cnt)]
        else:
            answer += alphabet[dis + cnt]
    return answer
"""
# s의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿔준다
# skip에 있는 알파벳은 제외하고 건너뛴다.
# index만큼 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다.
# 26개
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

s="bcdefghijklmnopqrstuvwxyz"
skip="a"
index=1

answer=''
for i in skip:
    alphabet.remove(i)

for i in s:
    answer+=alphabet[(alphabet.index(i)+index)%len(alphabet)]
print(answer)
"""
for i in s:
    a=ord(i)
    b=index
    while b>0:
        a+=1
        if a>ord('z'):
            a=ord('a')
        if chr(a) in skip:

            b+=1

        b-=1

    answer+=chr(a)
"""



