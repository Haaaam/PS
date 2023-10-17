def solution(n, words):
    say = []
    answer = [0, 0]

    for i in range(len(words)):
        if not say:
            say.append(words[i])
        else:
            if words[i] in say or say[-1][-1]!=words[i][0]:
                answer = [(len(say) % n + 1), (i // n + 1)]
                return answer
            elif say[-1][-1] == words[i][0]:
                say.append(words[i])


    return answer

# 1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다.
# 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말한다.
# 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 한다.
# 이전에 등장했던 단어는 사용 불가
# 한글자인 단어는 인정 x
# return 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구하기
# return [번호,차례]
n=2
words=["hello", "one", "even", "never", "now", "world", "draw"]

say=[]
answer=[0,0]
cnt=0
for i in range(len(words)):
    if not say:
        say.append(words[i])
    else:

        if words[i] in say:
            answer=[(len(say)%n+1),(i//n+1)]
            break
        elif say[-1][-1]==words[i][0]:
            say.append(words[i])
        elif say[-1][-1]!=words[-1][0]:
            answer=[(len(say)%n+1),(i//n+1)]
            break

print(answer)



