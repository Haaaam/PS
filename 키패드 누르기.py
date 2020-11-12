def dis(numbers,hand):
    dic={'1':(0,0),'2':(0,1),'3':(0,2),
         '4':(1,0),'5':(1,1),'6':(1,2),
         '7':(2,0),'8':(2,1),'9':(2,2),
         '*':(3,0),'0':(3,1),'#':(3,2)}
    hand=str(hand)
    numbers=str(numbers)
    xh,yh=dic[hand]
    xn,yn=dic[numbers]
    return abs(xh-xn)+abs(yh-yn)
def solution(numbers,hand):
    answer=''
    l='*'
    r='#'
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            l=i
        elif i in [3,6,9]:
            answer+='R'
            r=i
        elif i in [2,5,8,0]:
            ld=dis(l,i)
            rd=dis(r,i)
            if ld<rd:
                answer+='L'
                l=i
            elif ld>rd:
                answer+='R'
                r=i
            elif ld==rd:
                if hand=='right':
                    answer+='R'
                    r=i
                else:
                    answer+='L'
                    l=i
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))