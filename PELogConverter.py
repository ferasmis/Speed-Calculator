## Author: Feras
## Description: Speed calculator used for running distance in miles to get the speed in ft/s 

def milesToFt(miles):
    return  miles * 5280

def minToSecs(minutes):
    return minutes * 60

def speed(miles,minutes):
    return round(milesToFt(miles) / minToSecs(minutes),2)

miles = float(input("Enter miles:\n  "))
minutes = float(input("Enter time in mintues:\n  "))
print(speed(miles,minutes),"ft/s")