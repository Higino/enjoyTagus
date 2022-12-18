import sys
import os
import constants as const
from datetime import datetime
from datetime import timedelta
import re
import dateTime as dt


# Read command line arguments from sys.argv and validate file names and return List of file.
# Executing this program should in the form: python3 update.py inputFile1 inputFile2 inputFile3
# The return List should be the followng
#  [0] - is skypperfile
#  [1] - is requestsfile,
#  [2] - is schedulefile
# If the files do not conform to the file naming standard then the program needs to stop with an error message
def readCommandLineArguments():
    """
    Read command line arguments from sys.argv and validate file names and return List of file.
    Executing this program should in the form: python3 update.py inputFile1 inputFile2 inputFile3
     The return List should be the followng
          [0] - is skypperfile
          [1] - is requestsfile,
          [2] - is schedulefile
        If the files do not conform to the file naming standard then the program needs to stop with an error message
    """
    if( len(sys.argv) != 4 ):
        print("Error: Incorrect number of arguments. The program should be executed as: python3 update.py skypperfilepath requestsfilepath schedulefilepath")
        sys.exit(-1)

    skypperfile = sys.argv[1]
    requestsfile = sys.argv[2]
    schedulefile = sys.argv[3]
                 
    for fileArgIndex in range(1, 4):    
        # Check whether a path pointing to a file
        file = sys.argv[fileArgIndex]
        if os.path.isfile(file) != True:
            print("Error: File " + file + " does not exist.")
            sys.exit(-1)
    return (skypperfile, requestsfile, schedulefile)

# Initialization is done once only, so this as no effect if global variables are already set
def init(date, time):
    """
    This function initialises the program global variables CURRENT_RUN_DATETIME, LAST_RUN_DATETIME used throughout the program

    Requires: date and time are strings in the format "dd:mm:yyyy" and "hh:mm" respectively
    Ensures: CURRENT_RUN_DATETIME and LAST_RUN_DATETIME are set to the correct values
    """
    # If const are not set lets set them according to dates and times given as parameters
    if const.CURRENT_RUN_DATE != "" or const.LAST_RUN_DATE != "":
        # dates already set, we should keep them
        return 
    
    # Last run date and time are given as parameters
    const.LAST_RUN_DATE = date
    const.LAST_RUN_TIME = time
    
    # Compute current run date and time (which is 30 minutes after last run date unless it's a new day)
    if( dt.hourToInt(time) >= const.END_OF_DAY_INT_HOUR ):
        # This day is over we should start a new day based on todays date
        newTime = datetime.strptime(date, '%d:%m:%Y') + timedelta(days=1)
        const.CURRENT_RUN_DATE = newTime.strftime("%d:%m:%Y")
        const.CURRENT_RUN_TIME = const.START_OF_DAY_STRING_TIME
    else:
        currentMinute = int(const.LAST_RUN_TIME.split(":")[1])
        currentHour = int(const.LAST_RUN_TIME.split(":")[0])
        if currentMinute >= 30 and currentMinute < 60:
            const.CURRENT_RUN_TIME = dt.intToTime(currentHour+1, 0)
        else:
            const.CURRENT_RUN_TIME = dt.intToTime(currentHour, 30)
        # Since we are not in a new day, current run date is the same as last run date
        const.CURRENT_RUN_DATE = date


# Compute the next file names complete path according to requrements of file naming convention. 
# Next file names should be in the same directory structure and with the same name as redecessors as long as the time is increased by 30 minutes
# Returns the new computed file names and the dates that should go to the header of each file
def getNextFileNames(skippersFile, scheduleFile):
    """
    this function computes the next file names complete path according to requrements of file naming convention.

    Requires: skippersFile and scheduleFile are the full path of the files
    Ensures: Next file names should be in the same directory structure and with the same name as redecessors as long as the time is increased by 30 minutes
    """
    
    newFilesHour = dt.hourToInt(const.LAST_RUN_TIME)
    newFilesMinutes = 0
    headerDate = const.LAST_RUN_DATE
    if( const.LAST_RUN_TIME.split(":")[1] == "30"):
        newFilesMinutes = 0
        newFilesHour = dt.hourToInt(const.LAST_RUN_TIME) + 1
    else:
        newFilesMinutes = 30
    
    newFilesTime = headerTime = dt.intToTime(newFilesHour , newFilesMinutes)

    newSkippersFileName = re.sub("skippers.*", "skippers"+str(newFilesTime).replace(":", "h")+".txt", skippersFile)
    newScheduleFileName = re.sub("schedule.*", "schedule"+str(newFilesTime).replace(":", "h")+".txt", scheduleFile)
    return (newSkippersFileName, newScheduleFileName, headerDate, headerTime)   

           
