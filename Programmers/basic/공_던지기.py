
def solution(numbers,k):


    return numbers[2*(k-1)%len(numbers)]

numbers=[1,2,3,4,5,6]
k=5
print(numbers[2*(k-1)%len(numbers)])
