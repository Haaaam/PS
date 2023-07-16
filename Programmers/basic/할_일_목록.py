def solution(todo_list, finished):
    answer=[]
    for i in range(len(todo_list)):
        if finished[i]==False:
            answer.append(todo_list[i])

    return answer

todo_list=["problemsolving","practiceguitar","swim","studygraph"]
finished=[True,False,True,False]

print(solution(todo_list,finished))
