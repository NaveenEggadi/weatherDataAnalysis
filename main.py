'''import csv

with open("weather_data.csv") as weather:
    data = csv.reader(weather)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(data["temp"].mean())

print
print(data["condition"])
monday = data[data.day == "Monday"]
print(data[data.temp == data.temp.max()])
celsius = monday.temp
print((celsius * 9 / 5) + 32)

marks_list = {
    "students": ["ram", "sam", "nam"],
    "sores": [56, 78, 96]
}
data=pandas.DataFrame(marks_list)
data.to_csv("new_data.csv")'''

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
print(red_squirrel)
print(black_squirrel)
print(gray_squirrel)

data_dict = {"Fur Color": ["gray", "red", "black"],
             "Count": [gray_squirrel, red_squirrel, black_squirrel]}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
