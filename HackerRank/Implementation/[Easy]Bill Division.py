n,k=map(int,input().split())
bill=list(map(int,input().split()))
b=int(input())
res=0
def bonAppetit(bill, k, b):
    # Write your code here
    if b!=(sum(bill)-bill[k])/2:
        return int(b-(sum(bill)-bill[k])/2)
    else:
        return 'Bon Appetit'
print(bonAppetit(bill,k,b))