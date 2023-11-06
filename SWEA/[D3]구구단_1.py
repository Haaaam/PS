tc=int(input())
for i in range(tc):
    n=int(input())
    # n이 1이상 9이하의 두 수 a,b의 곱으로 표현될 수 있다면 "Yes", 아니면 "No"를 출력
    res="Yes"
    for j in range(1,10):
        if n%j==0:
            a=n//j
            if a<10 and a>=1:
                res="Yes"
                break
            else:
                res="No"
                continue

    print(f"#{i+1} {res}")