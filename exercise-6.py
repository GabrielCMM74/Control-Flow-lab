# exercise-06 What's the  Season?

month = input("Input the month of the year Jan - Dec: ")
day = int(input("Input the day: "))

if month in ('Jan', 'Feb', 'Mar'):
	season = 'winter'
elif month in ('Apr', 'May', 'Jun'):
	season = 'spring'
elif month in ('Jul', 'Aug', 'Sep'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'Mar') and (day > 19):
	season = 'spring'
elif (month == 'Jun') and (day > 20):
	season = 'summer'
elif (month == 'Sep') and (day > 21):
	season = 'autumn'
elif (month == 'Dec') and (day > 20):
	season = 'winter'

print("Season is",season)