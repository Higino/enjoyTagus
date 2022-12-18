import readingFromFiles
import constants as const
import writingToFiles as writter
import random
import utils
import scheduling
#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 221
# 60253 Hugo Silva 
# 60284 Kaisheng Li


skippersDict = {}

def getMatchingSkipper(availableSkippers, licenceType, language, speciality, requestTime):
    """
    function to unite drivers and customers

    Requires: availableSkippers is a dictionary of skippers, licenceType is a str, language is a list of str, speciality is a str, requestTime is a float
    Ensures:  returns a str with the name of the skipper that matches the criteria or an empty list if no skipper matches the criteria
    
    Extra function: We created a function to match a skipper with the customer's request. This function is called in the assign function.
    """
    matchedSkippersName = []
    for skipperName in availableSkippers:
        skipper = availableSkippers[skipperName]
        if skipperSpeaksLanguage(skipper["languages"], language) and skipper["licenceType"] == licenceType and skipper["speciality"] == speciality and float(skipper["timeMax"]) >= float(requestTime) + float(skipper["accumulatedTime"]):
            matchedSkippersName.append(skipperName)
    
    if len(matchedSkippersName) != 0:
        skipperIdx=random.randint(0, len(matchedSkippersName)-1)
        return matchedSkippersName[skipperIdx]
    else:
        return []

def skipperSpeaksLanguage(spokenLanguages, requiredLanguage):
    """
    this function checks if a skipper speaks the required language

    Requires: spokenLanguages is a list of str, requiredLanguage is a list of str
    Ensures:  returns True if the skipper speaks the required language or False if not
    
    Extra function reason: Utility function to check if a skipper speaks the required language. This function is called in the getMatchingSkipper function.
    """
    for l in spokenLanguages:
        for l1 in requiredLanguage:
            if( l == l1):
                return True
    return False


def assign(skippersFileName, scheduleFileName, requestsFileName):
    """
    Runs the enjoyTagus application.

    Requires:
    skippersFileName is a str with the name of a .txt file containing a list
    of skippers, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of cruises assigned to skippers as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested;
    these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the updated list of cruises assigned
    to skippers and the updated list of skippers, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    skippersXXhYY.txt, where XXhYY represents the time and date 30 minutes
    after the time and date indicated in the files skippersFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """

    # Read all the files
    skippersDict = readingFromFiles.readSkippersFile(skippersFileName)
    schedulesDict = readingFromFiles.readSchedulesFile(scheduleFileName)
    requestsList = readingFromFiles.readRequestsFile(requestsFileName)

    notAssignedList = [] # List of the requests that could not be matched to available skippers
    # For each request
    for request in requestsList:
        # Compute the matching skipper for the request criteria
        matchedSkipper = getMatchingSkipper(skippersDict,   request[const.REQUEST_SKIPPER_LICENCE_TYPE], 
                                                            request[const.REQUEST_CLIENT_LANGUAGES], 
                                                            request[const.REQUEST_SPECIALITY_TYPE], 
                                                            float(request[const.REQUEST_CRUISE_TIME]))
        if matchedSkipper == []:
            notAssignedList.append(const.CURRENT_RUN_DATE + ", "+const.NOT_ASSIGNED+", " + request[const.REQUEST_CLIENT_NAME_IDX])
            continue

        # Update the schedule. Give the matched skipper details, the request he was just assigned to and the existing schedules
        # this function returns the new schedule
        newSchedule = scheduling.getNewSchedule(skippersDict[matchedSkipper], request, schedulesDict)
        schedulesDict[newSchedule[const.SCHEDULE_DATE]+"|"+newSchedule[const.SCHEDULE_TIME]+"-"+matchedSkipper] = newSchedule
        
        # Update the skipper. Given the macthed skypper details return a new updated skipper record based on the travel request
        scheduling.updateSkipper(skippersDict[matchedSkipper], newSchedule)

    
    # Compute the next file names complete path according to requrements of file naming convention. 
    # Next file names should be in the same directory structure and with the same name as redecessors as long as the time is increased by 30 minutes
    (newSkippersFileName, newScheduleFileName, headerDate, headerTime) = utils.getNextFileNames(skippersFileName, scheduleFileName)
    # Compute the new files names. Replace the time in the file name with the time 30 minutes after the last run time


    # Save output files ( schedules, skippers) 
    writter.writeScheduleFile(schedulesDict, notAssignedList, newScheduleFileName, headerDate, headerTime)
    writter.writeSkippersFile(skippersDict, newSkippersFileName, headerDate, headerTime)

    return

""""
MAIN PROGRAM
"""

# Read command line arguments
(skippersFile, requestsFile, scheduleFile) = utils.readCommandLineArguments()
#(skippersFile, requestsFile, scheduleFile) = ("./data/testSet1/skippers17h00.txt", 
#                                    "./data/testSet1/requests17h00.txt",
#                                    "./data/testSet1/schedule17h00.txt")


# Assign skippers to requests
assign(skippersFile, scheduleFile, requestsFile)