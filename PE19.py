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
@author: Jason Baker
'''

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
                if year > 1900:
                    sumFirstSundays += 1;
                firstWeekday = 0;
            else:
                firstWeekday = weekdayOfLast + 1;
    return sumFirstSundays;

print(yearIter(1900, 2000));