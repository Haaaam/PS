# nxn크기의 단어 퍼즐을 만들려고 한다.
# return 특정 길이 k를 갖는 단어가 들어갈 수 있는 자리의 수
tc=int(input())
for t in range(tc):
    n,k=map(int,input().split()) # nxn 크기의 퍼즐, k: 특정 길이 k를 갖는 단어가 들어갈 수 있는 자리 수 출력

    array=[]
    for _ in range(n):
        array.append(list(map(int,input().split())))


    cnt=0
    for i in range(n):
        stack_row= []

        # 가로
        for j in range(n):
            if array[i][j]==0:
                if len(stack_row)==k:
                    cnt+=1
                stack_row=[]
            else:
                stack_row.append(array[i][j])
        if len(stack_row)==k:
            cnt+=1

    # 열
    for i in range(n):
        stack_col=[]
        for j in range(n):
            if array[j][i]==0:
                if len(stack_col)==k:
                    cnt+=1
                stack_col=[]
            else:
                stack_col.append(array[j][i])
        if len(stack_col)==k:
            cnt+=1


    print(f"#{t+1} {cnt}")