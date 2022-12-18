import constants as const
import sys
import utils
#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa



def removeHeader (fileName):
    """
    this function removes the header of a file

    Requires: fileName is a string with the name of the file
    Ensures: a list with the content of the file without the header
    """
    file = open(fileName, "r")
    filecontent = file.readlines()

    # Validate header
    nameOfFile = str(fileName).lower() # make sure is lower case so we can compare
    
    # File name must contain the type of file and the time of the file
    typeOfFileInHeader = filecontent[const.NUM_HEADER_LINES-1].rstrip().lower().split(":")[0] # Remove the : and the \n from the file line. Make sure is lower case
    
    headerDate = filecontent[const.NUM_HEADER_LINES-4].rstrip().lower()
    headerTime = filecontent[const.NUM_HEADER_LINES-2].rstrip().lower().replace(":", "h")
    
    # File name must contain the time of the header provided we replace the : with h to match time format
    if( headerTime.replace(":", "h") not in nameOfFile ):
        print ("Error: File " + fileName + " is not valid. The time of the file does not match the header.")
        file.close()
        sys.exit(-1)
    
    # File name must contain the type of file of the header
    if typeOfFileInHeader not in nameOfFile:
        print ("Error: File " + fileName + " is not valid. The name of the file does not match the header.")
        file.close()
        sys.exit(-1)
    
    # Now that we know which files we are reading we can compute the global auxiliary variables LASTRUN and CURRENTRUN datetimes
    # Initialization is done once only, so this as no effect if global variables are already set
    utils.init(headerDate, headerTime.replace("h", ":"))
    
    # The header date must match the date of last RUN. 
    if( str(headerDate) != str(const.LAST_RUN_DATE) or str(headerTime) != str(const.LAST_RUN_TIME).replace(":", "h")):
        print ("Error: File " + fileName + " is not valid. The date of the file "+headerDate+", "+headerTime+" does not match the last run date " + 
                const.LAST_RUN_DATE + ", " + const.LAST_RUN_TIME.replace(":", "h") + ".")
        file.close()
        sys.exit(-1)    
    
    # Header validated we can now remove the header    
    for x in range(const.NUM_HEADER_LINES):
        del filecontent[0]

    file.close()
    
    
    return filecontent





def readSkippersFile(fileName):
    """
    Reads a file with a list of skippers into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a skipper listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """
    inFile = removeHeader(fileName)

    skippersList = []
    for skipper in inFile:
        skipperData = skipper.rstrip().split(", ")
        skippersList.append(skipperData)
    
    skippersDict = {}
    for skipper in skippersList:
        if( skipper != "" ):
            # Fazer split da linha
            # Adicionar o skipper ao dicionario
            skippersDict[skipper[const.SKIPPER_NAME_IDX]]= {"name": skipper[const.SKIPPER_NAME_IDX], "licenceType": skipper[const.SKIPPER_LICENCE_TYPE], "languages": skipper[const.SKIPPER_LANGUAGES],
                                   "tariff": float(skipper[const.SKIPPER_TARIFF]), "speciality": skipper[const.SKIPPER_SPECIALITY], 
                                   "timeMax": float(skipper[const.SKIPPER_TIME_MAX]), "accumulatedTime": float(skipper[const.SKIPPER_ACCUMULATED_TIME]),
                                   "dateLastCruise": skipper[const.SKIPPER_DATE_LAST_CRUISE].replace("(", ""),
                                   "timeLastCruise": skipper[const.SKIPPER_TIME_LAST_CRUISE].replace(")", "")}
    return skippersDict


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested cruises with a given file name into a collection.

    Requires: fileName is str with the name of a .txt file containing
    a list of requested cruises organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    
    Ensures: list of lists where each list corresponds to a requested cruise listed in
    the file fileName (with all the info pieces belonging to that cruise),
    following the order provided in the lines of the file.

    
    """

    inFile = removeHeader(fileName)     

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        
   
    return requestsList


def readSchedulesFile (fileName):
    
    inFile = removeHeader(fileName)

    scheduleList = []
    for scheduleRaw in inFile:
        scheduleData = scheduleRaw.rstrip().split(", ")
        scheduleList.append(scheduleData)

    scheduleDict = {}
    for schedule in scheduleList:
        if( schedule != "" ):
            scheduleDict[schedule[const.SCHEDULE_DATE]+"|"+schedule[const.SCHEDULE_TIME]+"-"+schedule[const.SCHEDULE_SKIPPER_NAME]] = \
                        [schedule[const.SCHEDULE_DATE], \
                        schedule[const.SCHEDULE_TIME], \
                        schedule[const.SCHEDULE_DURATION], \
                        schedule[const.SCHEDULE_SKIPPER_NAME], \
                        schedule[const.SCHEDULE_PRICE], \
                        schedule[const.SCHEDULE_CLIENT_NAME]]

    return scheduleDict


