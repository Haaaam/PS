# our_score: 가채점한 점수
# score_list: 실제 성적이 번호 순서대로 담긴 정수 리스트
def solution(numbers, our_score,score_list):
    answer=[]
    for i in range(len(numbers)):
        if our_score[i]==score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")

    return answer