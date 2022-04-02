import datetime
import webbrowser
def firstHour():
    webbrowser.get("windows-default").open_new("https://www.explorelearning.com/")
    webbrowser.get("windows-default").open_new("https://earthobservatory.nasa.gov/")
    input()
def secHour():
    pass
def thirdHour():
    pass
def fourHour():
    webbrowser.get("windows-default").open_new("https://classroom.google.com/u/0")
    input()
    pass
def fifthHour():
    webbrowser.get("windows-default").open_new("https://deltamath.com/")
    input()
    pass
def sixthHour():
    webbrowser.get("windows-default").open_new("https://apod.nasa.gov/")
    webbrowser.get("windows-default").open_new("https://classroom.google.com/")
    input()
def sevHour():
    webbrowser.get("windows-default").open_new("https://classroom.google.com/")
    input()
rn = datetime.datetime.now()
rint = rn.time()
print(rn.strftime("The time is %I:%M %p")) 
def is_time_between(startTime,endTime):
    if startTime <= rint <= endTime:
        return endTime >= rint >= startTime
dotw = int(rn.strftime("%w"))