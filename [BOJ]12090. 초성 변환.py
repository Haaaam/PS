s=input()
#초성 리스트.00~18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
def sol(s):
    res=[]
    for i in list(s.strip()):
        if '가'<=i<='힣':
            #한글코드의 값(초성부분)=(초성*21)*28+0xAC00
            #'0xAC00'은 'ㄱ'의 코드값
            #초성=((x-0xAC00)//28)//21
            #중성의 갯수21, 종성의 갯수 28개로 이루어졌으므로 초성을 구하기 위해서 28*21한 것을 나눠줘야 한다.
            ch=((ord(i)-ord('가'))//28)//21
            res.append(CHOSUNG_LIST[ch])
        else:
            res.append([i])
    return res
for i in sol(s):
    print(i,end='')
