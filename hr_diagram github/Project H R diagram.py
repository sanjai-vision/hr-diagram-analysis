import pandas as pd

df = pd.read_csv("6 class csv.csv")

print(df.head())

print(df.info())

print(df.shape)

print(df.describe())

print(df.isnull().sum())
# df.dropna():remove the missing value entier row

print(df.duplicated().sum())#count duplicates

df = df.drop_duplicates()#remove duplicates

df.columns = df.columns.str.strip()#remove the space in column name

import matplotlib.pyplot as plt

#plt.boxplot(df["Temperature (K)"])
#plt.show()

print(df["Star type"].value_counts())

#plt.hist(df["Temperature (K)"], bins=20)
#plt.xlabel("Temperature")
#plt.ylabel("Count")
#plt.show()

plt.scatter(
    df["Temperature (K)"],
    df["Luminosity(L/Lo)"]
)

plt.gca().invert_xaxis()

plt.xlabel("Temperature (K)")
plt.ylabel("Luminosity")
plt.title("H-R Diagram")

plt.show()