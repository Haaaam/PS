def solution(num_list):
    cnt1,cnt2=0,0
    for i in num_list:
        if i % 2 == 0:
            cnt1 += 1
        else:
            cnt2 += 1
    return [cnt1,cnt2]

num_list=[1,2,3,4,5]
cnt1,cnt2=0,0

for i in num_list:
    if i%2==0: cnt1+=1
    else: cnt2+=1
print([cnt1,cnt2])