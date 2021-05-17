s=input()
time=s.split(':')
h,m,se=time[0],time[1],time[2]
if 'AM' in se:
    if h=='12':
        h='00'
    print(f"{h}:{m}:{se.split('AM')[0]}")

elif 'PM' in se:
    h=int(time[0])
    if h<12:
        h+=12
    h=str(h)
    print(f"{h}:{m}:{se.split('PM')[0]}")



