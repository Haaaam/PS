#2021.02.10
#[SWEA][D3]4406. 모음이 보이지 않는 사람

m=['a','e','i','o','u']
for i in range(int(input())):
    s=input()
    res=[j for j in s if j not in m]
    print(f"#{i+1} {''.join(res)}")

