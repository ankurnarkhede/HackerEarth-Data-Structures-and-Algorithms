import sys


def calculate_angle(hour, minute):
    # validate the input
    # minutes from 0 to 59
    if (hour < 0 or minute < 0 or hour > 12 or minute > 59):
        print ('Error in input!')
        exit (0)

    if (hour == 12):
        hour = 0
    if (minute == 60):
        minute = 0

    # calculating with reference to 12:00
    # angle covered by hour hand in one minute=360/(12*60)=0.5 degrees
    # angle covered by minute hand in one minute=360/60=6 degrees

    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    # calculating absolute difference
    angle = abs (hour_angle - minute_angle)
    return min (360 - angle, angle)


print ("Enter time in 12-hour format hh:mm")
hour, minute = (map (int, sys.stdin.readline ().strip ().split (':')))

print ('Angle = {}'.format (calculate_angle (hour, minute)))
