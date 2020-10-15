# MSID : M00795227
# 20152655
# YUEN WAI YIP

#1 Mailing address
print("\nQ1.Mailing address")
print("YUEN WAI YIP")
print("1 Queen's Road Central, Hong Kong")
print("GPO Box 64 Hong Kong")
print("Hong Kong")


#2 Area and perimeter of a rectangle
print("\nQ2.Area and perimeter of a rectangle")
width = 4.5
height = 7.9
area = formatted_float = "{:.2f}".format(width * height)
perimeter = "{:.2f}".format(2*(width+height))
print("area" , (area))
print("perimeter" , perimeter)

#3.Average speed of a runner
print("\nQ3.Average speed of a runner")
disMiles = 14 / 1.6 
timeSec = 45 * 60 + 30
avgSpeedPerHour = "{:.2f}".format(disMiles/timeSec * 60 * 60)
print("average speed in miles per hour: " + str((avgSpeedPerHour)) + " miles per hour");

#4.Time of watching Netflix series
print("\nQ4.Time of watching Netflix series")
totalSecfirstSeason = (45*60 + 35) * 10
totalSecOtherSeason = (35*60 + 15) * 10 * 4

totalSec = totalSecfirstSeason + totalSecOtherSeason
totalHour = "{:.2f}".format(totalSec / 60 / 60 )
print("how long (in unit of hours) would take you to watch nonstop Netflix series?", (totalHour),"Hours" )

#5.Convert pounds into kilograms
print("\nQ5.Convert pounds into kilograms")
pound = float(input("Enter a value in pounds:"))
kilo = pound * 0.454
print(pound," pounds is ",kilo, "kilograms")

#6.Convert feet into meters
print("\nQ6.Convert feet into meters")
feet = float(input("Enter a value for feet:"))
meters = feet * 0.305
print(feet," feet is ",meters, "meters")

#create a computational problem
print("\ncomputational problem")
birth = 7
dead = 13
new = 45
nowPpl = 312032486
day = 365
secInYear = day * 24 * 60 * 60
newPplInYear = int(secInYear/birth) - int(secInYear/dead) + int(secInYear/new)
Year1 = nowPpl + newPplInYear
Year2 = Year1 + newPplInYear
Year3 = Year2 + newPplInYear
Year4 = Year3 + newPplInYear
Year5 = Year4 + newPplInYear
print("The population of next 1 year is:", Year1)
print("The population of next 2 years is:", Year2)
print("The population of next 3 years is:", Year3)
print("The population of next 4 years is:", Year4)
print("The population of next 5 years is:", Year5)






