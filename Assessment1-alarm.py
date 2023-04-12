#   Nicolas Callier
#   CSCI101 - Section D
#   Python Assessment
#   References: Student Sean
#   Time: 25 minutes

early = int(input("How many minutes early would you like your alarm to go off?\n EARLY> "))
hours = int(input("What time do you need to get out of bed?\n HOURS> "))
mins = int(input("MINUTES> "))

def AnnoyingAlarm(i, j, k):
    aHours = i
    aMins = j - k
    while aMins < 0:
        aHours -= 1
        aMins += 60
        if aHours < 0:
            aHours = 23
    if len(str(aHours)) < 2:
        aHours = "0" + str(aHours)
    if len(str(aMins)) < 2:
        aMins = "0" + str(aMins)
    return([str(aMins), str(aHours)])

print("You should set your alarm for:\n OUTPUT " + AnnoyingAlarm(hours, mins, early)[1] + " " + AnnoyingAlarm(hours, mins, early)[0])
