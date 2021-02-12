book=[input() for _ in range(int(input()))]
book_count={}

for i in book:
    if i in book_count:
        book_count[i]+=1
    else:
        book_count[i]=1
target=max(book_count.values())
res=[]
for b,c in book_count.items():
    if target==c:
        res.append(b)
print(sorted(res)[0])

