def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special_characters='!@#$%^&*()-+'
    cnt=0
    #any(iterableValue): 전달받은 자료형의 element 중 하나라도 True일 경우 True를 반환
    #만약 empty 값을 argument로 넘겨주면 False를 반환
    if any(i.isdigit() for i in password)==False:
        cnt+=1
    if any(i.islower() for i in password)==False:
        cnt+=1
    if any(i.isupper() for i in password)==False:
        cnt+=1
    if any(i in special_characters for i in password)==False:
        cnt+=1
    return max(cnt,6-n)
n=int(input())
password=input()
print(minimumNumber(n,password))
