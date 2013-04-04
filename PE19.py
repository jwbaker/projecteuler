'''
Created on 2013-04-03

Problem 19:
You are given the following information, but you may prefer to do some research for yourself.
- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone.
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many SUndays fell on the first of the month during the twentieth century (1 Jan 1901 to 21 Dec 2000)?

SOLUTION: 171
@author: Jason Baker
'''

# This algorithm is really just based off pattern matching from looking at a calendar
# In months with 30 days, the last day of the months is always one weekday after the first of the month
# In months with 31 days, it's two weekdays (This should be obvious)
# In February on leap years, the weekdays are the same (This should also be obvious)
# In February on non-leap years, the last of the month is the weekday before the first (This as well should be obvious)
def procMonth(month, isLeap, weekdayOfFirst):
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"];
    lastOfMonth = 0;
    
    if months[month] == "april" or months[month] == "june" or months[month] == "september" or months[month] == "november":
        lastOfMonth = (weekdayOfFirst + 1) % 7;
    elif months[month] == "february":
        if isLeap:
            lastOfMonth = weekdayOfFirst;
        else:
            lastOfMonth = (weekdayOfFirst - 1) % 7;
    else:
        lastOfMonth = (weekdayOfFirst + 2) % 7;
    
    return lastOfMonth;

# Just iterate through every year and month, and process each month
# The procMonth method is O(1), so this isn't too bad in terms of performance
def yearIter(start, end):
    firstWeekday = 1;
    sumFirstSundays = 0;
    for year in range(start, end + 1):
        leap = False;
        if year % 100 == 0 and year % 400 == 0:
            leap = True;
        elif year % 4 == 0:
            leap = True;
        
        for month in range(0, 12):
            weekdayOfLast = procMonth(month, leap, firstWeekday);
            if weekdayOfLast == 6:
                # We need to start iterating at 1900 because the question didn't tell us what the first weekday of 1901 is
                # But we also don't care about Sundays in 1900, so we ignore them for summing
                if year > start:
                    sumFirstSundays += 1;
                firstWeekday = 0;
            else:
                firstWeekday = weekdayOfLast + 1;
    return sumFirstSundays;

print(yearIter(1900, 2000));