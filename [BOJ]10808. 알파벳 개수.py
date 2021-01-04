#10808. 알파벳 개수
n=input()
for i in range(97,123):
  print(n.find(chr(i)),end=' ')