def playingWithDates(dates):
    year = dates[-4:]
    month = str(dates[-8:-5])
    day = ''

    for i in range(len(dates)):
        if dates[i].isalpha():
            break
        elif dates[i].isnumeric():
            day = day + dates[i]

    if len(day) == 1:
        day = '0' + day

    month_conv = {
        'Jan' : '01',
        'Feb' : '02',
        'Mar' : '03',
        'Apr' : '04',
        'May' : '05',
        'Jun' : '06',
        'Jul' : '07',
        'Aug' : '08',
        'Sep' : '09',
        'Oct' : '10',
        'Nov' : '11',
        'Dec' : '12'
    } 

    month_num = month_conv[month]

    final_date = year + '-' + month_num + '-' + day

    return final_date

print(playingWithDates('22nd Jan 2013'))

