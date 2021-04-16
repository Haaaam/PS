#a:낮에 올라가는 거리, b:밤에 미끄러지는 거리, v:높이
a,b,v=map(int,input().split())
res=(v-b)/(a-b)
print(int(res) if res==int(res) else int(res)+1)

