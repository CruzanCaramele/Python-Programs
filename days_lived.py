###
### this a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def isleapyear(year):
    if year % 4 == 0 and year % 100 != 0: 
        return True
    else: 
        return False

def nextDay(year, month, day):
    if isleapyear(year): 
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else: 
        months = [31,28,31,30,31,30,31,31,30,31,30,31]

    if day < months[month-1]:
       return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False 


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    #CODE HERE!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        days = days + 1
        (year1, month1, day1) = nextDay(year1, month1, day1)    
    return days
        
        



















    

    
    
