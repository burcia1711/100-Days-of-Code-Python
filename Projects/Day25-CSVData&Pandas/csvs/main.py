#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)


import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)
average_temp = sum(temp_list)/len(temp_list)
print(average_temp)
print(data['temp'].mean())
print(data['temp'].max())

#get data in columns
print(data["condition"])
print(data.condition)

#get data in rows
print(data["day"])
print(data[data.day == 'Monday'])
monday = data[data.day == 'Monday']

print(monday.temp*(9/5)+32) #Monday's temps in Fahrenheit

print(data[data.temp == data['temp'].max()])

#create a data frame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_new = pandas.DataFrame(data_dict)
data_new.to_csv("data_new.csv")
