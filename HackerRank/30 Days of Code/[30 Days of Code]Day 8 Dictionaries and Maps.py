n = int(input())
phoneBook = dict()
for i in range(n):
    name, pn = input().split()
    phoneBook[name] = pn

while True:
    try:
        nn = input()
        phone_number = phoneBook.get(nn)
        if phone_number:
            print(nn + '=' + phoneBook[nn])
        else:
            print('Not found')
    except EOFError:
        break

