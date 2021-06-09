def dayOfProgrammer(year):
    if year%4==0:
        return "12.09."+str(year)
    else:
        return "13.09."+str(year)

year=int(input())
print(dayOfProgrammer(year))