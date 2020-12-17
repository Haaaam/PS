#from collections import Counter
#n:가지고 있는 숫자 카드 갯수
#m: 주어진 정수의 갯수
#n=int(input())
#l1=list(map(int,input().split()))
#m=int(input())
#l2=list(map(int,input().split()))
#l1=Counter(l1)
#for i in l2:
#    print(l1[i],end=' ')
import sys
input=sys.stdin.readline
n=int(input())
l1=list(map(int,input().split()))
l1.sort()
m=int(input())
l2=list(map(int,input().split()))
def binary_search(array,target,s,e):
    while s<=e:
        mid=(s+e)//2
        if array[mid]==target:
            return array[s:e+1].count(target)
        elif array[mid]>target:
            e=mid-1
        else:
            s=mid+1
    return None

e_dic={}
for i in l1:
    s=0
    e=len(l1)-1
    if i not in e_dic:
        e_dic[i]=binary_search(l1,i,s,e)
print(' '.join(str(e_dic[x])if x in e_dic else '0'for x in l2))