#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa


def addHoursToDateTime(dateTime, hours):
    """
        Function adds a time to a datetime.It only adds hours not minutes
        Requires: DateTime in the format "dd:mm:yyyy|hh:mm" and hour is the integer representing the number of hours to add. 
                  Unfortunately no validation is done on the dateTime format after adding the hours as it can be bigger than 24.
                  In that case the date will be wrong
        Ensures: Returns a string with the new date and time in the format "dd:mm:yyyy|hh:mm"
    """
    date1 = (dateTime.split("|")[0], dateTime.split("|")[1])
    time1 = (date1[1].split(":")[0], date1[1].split(":")[1])
    
    newHour = hourToInt(time1[0]) + hours
    newHourString = intToTime(newHour, int(time1[1]))
    return date1[0] + "|" + newHourString 



def biggestDate(dateTime1, dateTime2):
    """
    This function takes two dates and times and returns the biggest one.
    
    Requires: The dates and times to be in the format: dd:mm:yyyy|hh:mm
    
    Ensures: When the dates are the same, the function returns one of them
    
    """
    date1 = dateTime1.split("|")[0]
    date2 = dateTime2.split("|")[0]
    day1 = date1.split(":")[0]
    month1 = date1.split(":")[1]
    year1 = date1.split(":")[2]
    day2 = date2.split(":")[0]
    month2 = date2.split(":")[1]
    year2 = date2.split(":")[2]
    time1 = dateTime1.split("|")[1]
    time2 = dateTime2.split("|")[1]
    hour1 = time1.split(":")[0]
    min1 = time1.split(":")[1]
    hour2 = time2.split(":")[0]
    min2 = time2.split(":")[1]

    if date1 == date2 :
        if int ( hour1 + min1 )  >  int( hour2 + min2 ):
            return dateTime1
        else:
            return dateTime2
        
    else:
        if int(year1+month1+day1) > int(""+year2+month2+day2):
            return dateTime1
        else:
            return dateTime2
 
#funcao extra
def dateToInt(date):
    """
    this function takes a date in the format dd:mm:yyyy and returns the date as an integer
    
    Requires: date in the format dd:mm:yyyy
    Ensures: returns the date as an integer
    """
    t=date.split(":")
    t1 = int(str(t[0]) + str(t[1]) + str(t[2]))
    return t1    
    
def hourToInt(time):
    """
    this function takes a time in the format hh:mm and returns the hour as an integer
    Requires: time in the format hh:mm
    Ensures: returns the hour as an integer
    """
    t = time.split(":")
    return int(t[0])



def minutesToInt(time):
    """
    this function takes a time in the format hh:mm and returns the minutes as an integer
    Requires: time in the format hh:mm
    Ensures: returns the minutes as an integer
    """
    t = time.split(":")
    return int(t[1])    


def intToTime(hour, minutes):
    """
    this function takes an hour and minutes and returns a string with the time in the format hh:mm
    Requires: hour and minutes as integers
    Ensures: returns a string with the time in the format hh:mm
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m










