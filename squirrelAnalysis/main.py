import csv
import pandas
import pandas as pd

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur = data["Primary Fur Color"]
fur_count = fur.value_counts()
fur_count_list = [{"fur color": color, "count": count} for color, count in fur_count.items()]

print(fur_count_list)
file = pd.DataFrame(fur_count_list)
file.to_csv("Squirrel_Census_-_Squirrel_Data.csv", index = True)