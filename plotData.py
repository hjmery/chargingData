import datetime

#opening up the file and reading everything into a data matrix
file = open('C:/Users/hjmer/Dropbox/USUFall2019/MachineLearningTA/ForFlann/2019/07/ChargeIntervals-2019-07-30.csv')
data = []

for i in file.readlines():
    i = i.split(',')
    data.append(i)

plugInTimeInitial = []
plugOutTimeInitial = []
plugInTime = []
plugOutTime = []

for i in data[1:]:
    plugInTimeInitial.append(i[7])
    plugOutTimeInitial.append(i[8])

for i in range(len(plugInTimeInitial)):
	if plugInTimeInitial[i] != '':
		plugInTime.append(plugInTimeInitial[i])
	if plugOutTimeInitial[i] != '':
		plugOutTime.append(plugOutTimeInitial[i])

print(plugInTime[1][-8:])

print(plugInTime)
print(plugOutTime)

plugIndatetime = []
plugOutdatetime = []

for i in plugInTime:
	month = int(i[0])
	day = int(i[2:4])
	year = int(i[5:9])
	hour = int(i[-8:-6])
	minute = int(i[-5:-3])
	second = int(i[-2:])
	#print(month, day, year, hour, minute, second)
	plugIndatetime.append(datetime(month, day, year, hour, minute, second))

file.close()