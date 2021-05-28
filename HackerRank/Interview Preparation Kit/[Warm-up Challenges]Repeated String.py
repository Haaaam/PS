s=list(input())
n=int(input())


def repeatedString(s, n):
    # Write your code here

    return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')
print(repeatedString(s,n))