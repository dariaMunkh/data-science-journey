import pandas as pd 

#---------------- Series ----------------#
# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#          Think of it like a single column inn a spreadsheet (1-Dimensional)

data = [100, 102, 104]
data1 = [200, 202, 204]
# Constructor Series
series = pd.Series(data)

print(series)
print()

series1 = pd.Series(data1, index=["a", "b", "c",])
print(series1)

series1.loc["a"] = 180
print(series1.loc["a"])
print(series1.iloc[1])

# Dicitonary made with key value pairs
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
series2 = pd.Series(calories)
print(series2)
print()

# Access Day 3 and adjust the value 
series2.loc["Day 3"] += 500
print(series2.loc["Day 3"])
print()

print(series2[series2 >= 2000])