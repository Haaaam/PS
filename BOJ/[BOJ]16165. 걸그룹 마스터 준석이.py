n,m=map(int,input().split())

team_mem,mem_team={},{}

for i in range(n):
    team_name,mem_num=input(),int(input())
    team_mem[team_name]=[]
    for j in range(mem_num):
        mem_name=input()
        team_mem[team_name].append(mem_name)
        mem_team[mem_name]=team_name
for _ in range(m):
    prob_name=input()
    prob=int(input())
    if prob:
        print(mem_team[prob_name])
    else:
        for i in sorted(team_mem[prob_name]):
            print(i)


