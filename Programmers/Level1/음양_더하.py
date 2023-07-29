def solution(absolutes, signs):
    sum=0
    for i in range(len(absolutes)):
        if signs[i]==True:
            sum+=absolutes[i]
        elif signs[i]==False:
            sum-=absolutes[i]
    return sum


absolutes=[4,7,12]
signs=[True,False,True]
print(solution(absolutes,signs))

