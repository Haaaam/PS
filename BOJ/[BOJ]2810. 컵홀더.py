n=int(input())
seat=input()
l=len(seat)
seat=seat.replace('S','*')
seat=seat.replace('LL','*')

if l<=len(seat):
    print(l)
else:
    print(len(seat)+1)

