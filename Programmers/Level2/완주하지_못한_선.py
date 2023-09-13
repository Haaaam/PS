def solution(participant, completion):
    dict = {}
    for i in participant:
        if i not in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
    for i in completion:
        if i in dict:
            dict[i] -= 1

    for k, v in dict.items():
        if v != 0:
            return k


participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]
print(solution(participant,completion))


# 효율성(시간 초과)
"""
while len(completion)!=0:
    for i in completion:
        if i in participant:
            completion.remove(i)
            participant.remove(i)
"""

