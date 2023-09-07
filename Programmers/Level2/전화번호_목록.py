# 해시 알고리즘
def solution(phone_book):
    answer = True
    hash = {}
    for i in phone_book:
        hash[i] = 1

    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            if temp in hash and temp != i:

                answer = False
                break
    return answer

phone_book=["123", "456", "789"]

answer=True
print(solution(phone_book))
