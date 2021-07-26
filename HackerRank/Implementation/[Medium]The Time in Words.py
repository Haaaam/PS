def sol(h,m):
    hours = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    minutes = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
               'eighteen', 'ninteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four',
               'twenty five',
               'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
    tmp = {0: "%s o' clock",
           1: "one minute past %s",
           10: "ten minutes past %s",
           15: "quarter past %s",
           30: "half past %s",
           40: "twenty minutes to %s",
           45: "quarter to %s"}

    time = ""

    if m in (0, 1, 10, 15, 30, 40, 45):
        a = 1 if m <= 30 else 0
        time = tmp[m] % hours[h - a]

    elif m < 30:
        hour = hours[h - 1]
        time = f'{minutes[m - 1]} minutes past {hour}'

    elif m > 30:
        hour = hours[h]
        time = f'{minutes[60 - m - 1]} minutes to {hour}'

    return time


h,m=int(input()),int(input())
print(sol(h,m))