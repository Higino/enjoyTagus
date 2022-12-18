#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa
import constants as const
import dateTime as dt


# Update the skipper. Given the macthed skypper details return a new updated skipper record based on the travel request
def updateSkipper(skipperRecord, schedule):
   """
    this function updates the skipper record with the new trip details
    Requires: skipperRecord is a dictionary with the skipper details and schedule is a list with the schedule details
    Ensures: a new skipper record is returned as a dictionary
    
    Extra function reason: We need to update the skipper record with the new trip details. Function given in skeleton code was to 
    update all the skipper records with the new trip details. We only need to update one skipper record
   """
   # Add accumulated time to the skipper record
   skipperRecord["accumulatedTime"] += float(schedule[const.SCHEDULE_DURATION])
   # Add last trip from schedule to the skipper record
   skipperRecord["dateLastCruise"] = schedule[const.SCHEDULE_DATE]
   skipperRecord["timeLastCruise"] = schedule[const.SCHEDULE_TIME]



# Update the schedule. Give the matched skipper details, the request he was just assigned to and the existing schedules
# this function returns the new schedule
def getNewSchedule(skippersRecord, request, schedulesDict):
    """
    Update the schedule. Give the matched skipper details, the request he was just assigned to and the existing schedules
        this function returns the new schedule
    Requires: skippersRecord is a dictionary with the skipper details, request is a list with the request details and schedulesDict is a dictionary with the existing schedules
    Ensures: a new schedule is returned as a list
    Extra function reason: We need to get the new schedule for the skipper.
    """
    # If no trip has been assigned to this skipper yet, then the new trip will be at the current run date and time
    dateTimeOfLastTrip = const.CURRENT_RUN_DATE+"|"+const.CURRENT_RUN_TIME
    for key in schedulesDict.keys():
        if skippersRecord["name"] == key.split("-")[1]: 
            if dt.biggestDate(key.split("-")[0], dateTimeOfLastTrip) != dateTimeOfLastTrip:
                dateTimeOfLastTrip = key.split("-")[0]
    if( dateTimeOfLastTrip == const.CURRENT_RUN_DATE+"|"+const.CURRENT_RUN_TIME):
        # No trip has been assigned to this skipper yet, create the trip in the schedule assigning it a key
        schedulesDict[dateTimeOfLastTrip+"-"+skippersRecord["name"]] = []
        newTripDateTime = dateTimeOfLastTrip
    else:
        # A trip has been assigned to this skipper, get the last trip and add the cruise duration to it
        lastSchedule = schedulesDict[dateTimeOfLastTrip+"-"+skippersRecord["name"]]
        newTripDateTime = dt.addHoursToDateTime(dateTimeOfLastTrip, int(lastSchedule[2]))
        
    # Now compute the new schedule attributes
    newSchedule = ["","","","","",""]
    newSchedule[const.SCHEDULE_TIME] = newTripDateTime.split("|")[1] #new time 
    newSchedule[const.SCHEDULE_SKIPPER_NAME] = skippersRecord["name"] #skipper name
    newSchedule[const.SCHEDULE_PRICE] = skippersRecord["tariff"] #tariff
    newSchedule[const.SCHEDULE_CLIENT_NAME] = request[const.REQUEST_CLIENT_NAME_IDX] # client name
    newSchedule[const.SCHEDULE_DATE] = newTripDateTime.split("|")[0]#new date
    newSchedule[const.SCHEDULE_DURATION] = request[const.REQUEST_CRUISE_TIME] #new cruise duration duration

    return newSchedule


def updateSkippers(skippers, schedule):
    """We dont need this function because we just need to update one skipper not all of them"""
    return None



