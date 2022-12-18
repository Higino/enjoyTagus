#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 546
# 65000 Óscar Adalberto 
# 65015 Miquelina Josefa



# This module records the constants used in the application

# You should define here as many constants as you need to keep your 
# code clean and legible



# Value for skipper's name in a task not assigned in the output schedule
NOT_ASSIGNED = "not-assigned"

#HOURS References
END_OF_DAY_INT_HOUR = 20
START_OF_DAY_STRING_TIME = "08:00"

#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 221
# 60253 Hugo Silva 
# 60284 Kaisheng Li


# Global variables that are immutable once set
LAST_RUN_DATE=""
LAST_RUN_TIME=""
CURRENT_RUN_DATE=""
CURRENT_RUN_TIME=""

# In a file:
# Number of header's lines
NUM_HEADER_LINES = 7


# In a skipper's list:
# Index of the element with the skipper's name
SKIPPER_NAME_IDX = 0
SKIPPER_LICENCE_TYPE = 2
SKIPPER_LANGUAGES = 1
SKIPPER_TARIFF = 3
SKIPPER_SPECIALITY = 4
SKIPPER_TIME_MAX = 5
SKIPPER_ACCUMULATED_TIME = 6
SKIPPER_DATE_LAST_CRUISE = 7
SKIPPER_TIME_LAST_CRUISE = 8

# In a cruise's list:
# Index of the element with the client's name
REQUEST_CLIENT_NAME_IDX = 0
REQUEST_CLIENT_LANGUAGES = 1
REQUEST_SKIPPER_LICENCE_TYPE = 2
REQUEST_SPECIALITY_TYPE = 3
REQUEST_CRUISE_TIME = 4

# In a shedule list:
# Index of the element with the name
SCHEDULE_DATE = 0
SCHEDULE_TIME = 1
SCHEDULE_DURATION = 2
SCHEDULE_SKIPPER_NAME = 3
SCHEDULE_PRICE = 4
SCHEDULE_CLIENT_NAME = 5