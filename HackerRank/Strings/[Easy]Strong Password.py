def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special_characters='!@#$%^&*()-+'
    cnt=0
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
