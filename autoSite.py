#gonna have a doc that has the set list of values. Defaulting at the standard 8 45-minute-periods.
#Block periods (Wed and Thu) will be 1 hour and 30 minutes by default, except 5th/4th on block, as they are used for lunch.
#this doc will serve as the customization menu, making the values typed define the required values in this file.
from datetime import time
import autoSiteSystems as ass
from time import sleep

if ass.dotw == 3:
    if ass.is_time_between(time(8,00), time(9,30)):
        print("It's 1st Hour.")
        ass.firstHour()
    elif ass.is_time_between(time(9,35), time(11,5)):
        print("It's 3rd Hour.")
        ass.thirdHour()
    elif ass.is_time_between(time(11,10), time(13,20)):
        print("It's 5th Hour.")
        ass.fifthHour()
    elif ass.is_time_between(time(13,30), time(15,00)):
        print("It's 7th Hour.")
        ass.sevHour()
    elif ass.rint > time(15,00):
        print("It's after school!")
        sleep(5)
    elif ass.rint < time(8,00):
        print("It's before school.")
        sleep(5)
    else:
        print("It's passing period!")
        sleep(5)
if ass.dotw == 4:
    if ass.is_time_between(time(8,00), time(9,30)):
        print("It's 1st Hour.")
        ass.firstHour()
    elif ass.is_time_between(time(9,35), time(11,5)):
        print("It's 3rd Hour.")
        ass.thirdHour()
    elif ass.is_time_between(time(11,10), time(13,20)):
        print("It's 5th Hour.")
        ass.fifthHour()
    elif ass.is_time_between(time(13,30), time(15,00)):
        print("It's 7th Hour.")
        ass.sevHour()
    elif ass.rint > time(15,00):
        print("It's after school!")
        sleep(5)
    elif ass.rint < time(8,00):
        print("It's before school.")
        sleep(5)
    else:
        print("It's passing period!")
        sleep(5)
else:
    if ass.is_time_between(time(8,00), time(8,45)):
        print("It's 1st Hour.")
        ass.firstHour()
    elif ass.is_time_between(time(8,50), time(9,35)):
        print("It's 2nd Hour.")
        ass.secHour()
    elif ass.is_time_between(time(9,40), time(10,25)):
        print("It's 3rd Hour.")
        ass.thirdHour()
    elif ass.is_time_between(time(10,30), time(11,15)):
        print("It's AI!")
    elif ass.is_time_between(time(11,20), time(12,28)):
        print("It's 4th Hour.")
        ass.fourHour()
    elif ass.is_time_between(time(12,33), time(13,19)):
        print("It's 5th Hour.")
        ass.fifthHour()
    elif ass.is_time_between(time(13,22), time(14,10)):
        print("It's 6th Hour.")
        ass.sixthHour()
    elif ass.is_time_between(time(14,13), time(15,1)):
        print("It's 7th Hour.")
        ass.sevHour()
    elif ass.rint > time(15,1):
        print("It's after school!")
        sleep(5)
    elif ass.rint < time(7,49):
        print("It's before school.")
        sleep(5)
    else:
        print("It's passing period!")
        sleep(5)