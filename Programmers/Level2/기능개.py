# 각 progresses가 완료된 시간을 구해서 푸는 방법으로 접근

def solution(progresses, speeds):
    answer=[]
    done = [(100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else ((100 - progresses[i]) //
                                                                                               speeds[i]) + 1 for i in
            range(len(progresses))]
    # 5 10 1 1 20 1

    while done:
        cnt = 1
        a = done.pop(0)  # 1번째 원소 꺼내기

        while True:

            if not done:
                break

            if a >= done[0]:
                done.pop(0)
                cnt += 1
            else:
                break
        answer.append(cnt)
    return answer

progresses=[93, 30, 55]
speeds=[1, 30,5]
answer=[]

done=[(100-progresses[i])//speeds[i] if (100-progresses[i])%speeds[i]==0 else ((100-progresses[i])//speeds[i])+1 for i in range(len(progresses))  ]
# 5 10 1 1 20 1
n=len(progresses)
while done:
    cnt=1
    a=done.pop(0) # 1번째 원소 꺼내기

    while True:

        if not done:
            break

        if a>done[0]:
            done.pop(0)
            cnt+=1
        else:
            break
    answer.append(cnt)

print(answer)


