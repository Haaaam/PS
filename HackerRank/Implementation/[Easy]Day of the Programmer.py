def dayOfProgrammer(year):
    if year==1918:
        return "26.09.1918"
    elif (year<1918 and year%4==0) or (year>1918 and year%400==0 or  (year%4==0 and year%100!=0)):
        return "12.09."+str(year)
    else:
        return "13.09."+str(year)

year=int(input())
print(dayOfProgrammer(year))