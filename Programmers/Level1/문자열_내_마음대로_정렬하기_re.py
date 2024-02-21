# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순
# ex) strings가 ["sun","bed","car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u","e","a"로 strings를 정렬

def solution(strings,n):
    answer=[]
    return sorted(sorted(strings) ,key=lambda x:x[n])

strings=["abce", "abcd", "cdx"]
n=1
print(solution(strings,n))