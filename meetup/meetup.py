import calendar
from datetime import date


def meetup_day(year, month, weekDay, weekName):
    dayDict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
               'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    weekNameDict = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4,
                    'last': -1, 'teenth': None}
    meetupMonth = calendar.monthrange(year, month)
    days = range(0, 7)*6
    days = days[meetupMonth[0]:]
    days = days[:meetupMonth[1]]

    weekNumber = dayDict[weekDay]
    allMonthDays = [i for i, x in enumerate(days, 1) if x == weekNumber]

    if weekName != 'teenth':
        day = allMonthDays[weekNameDict[weekName]]
    else:
        print 'working'
        day = [x for x in allMonthDays if 20 > x > 9][0]
    return date(year, month, day)