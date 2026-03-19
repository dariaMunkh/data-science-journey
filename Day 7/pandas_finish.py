import pandas as pd 

#-------------- Selection -------------#
df = pd.read_csv("Day 6\pokemon.csv")

# Selection by Column
print(df["Name"].to_string())
print(df["Height"].to_string())
print()
print(df[["Name", "Height", "Weight"]].to_string)
print()

# Selection by Row 
print(df.loc[0])
print(df.loc[6,["Height", "Weight"]])
print(df.iloc[:11:2, 0:3])
print()
#------------------ Filtering -------------#
# Filtering = Keeping the rows that match a condition

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] >= 100]
legendary_pokemon = df[df["Legendary"] == 1]
water_pokemon = df[(df["Type1"] == "Water") |
                    (df["Type2"] == "Water")]
print(tall_pokemon)
print()
print(heavy_pokemon)
print()
print(legendary_pokemon)
print()
print(water_pokemon)
print()

#------------------ Aggregation ------------------#
# Aggregate functions = reduce a set of values into a single summary value
#                       used to summarize and analyze data 
#                       often used with the groupby() function

# Whole dataframe
print("Mean")
print(df.mean(numeric_only=True))
print("Sum")
print(df.sum(numeric_only=True))
print("Min")
print(df.min(numeric_only=True))
print("Max")
print(df.max(numeric_only=True))
print("Count")
print(df.count())

# Single columnprint("Mean")
print("Mean")
print(df["Height"].mean())
print("Sum")
print(df["Height"].sum())
print("Min")
print(df["Height"].min())
print("Max")
print(df["Height"].max())
print("Count")
print(df["Height"].count())

group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())

#--------------------- Data Cleaning ----------------#

# Data cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.

# 1. Drop irrelevant columns
#df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data
#df = df.dropna(subset=["Type2"])
#df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                   "Fire": "FIRE",
#                                   "Water": "WATER"})

# 4. Standardize text
df["Name"] = df["Name"].str.lower()

# 5. Fix data types
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
# df = df.drop_duplicates()

print(df.to_string())