import csv
import pandas

# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data.temp.mean())
# print(data["temp"].max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_tempf = monday_temp * 9/5 + 32
# print(monday_tempf)

#create a dataframe from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores":[12,42,100]
# }
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_fur_count = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur color": ["Gray", "Cinnamon", "White"],
    "count": [gray_fur_count, Cinnamon_fur_count, Black_fur_count]
}
print(data_dict)
data2 = pandas.DataFrame(data_dict)
data2.to_csv("squirrel_count.csv")
