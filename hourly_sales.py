import pandas as pd

# Load the Data sheet
df = pd.read_excel("bakery.xlsx", sheet_name="Data")

# SUMIF equivalent: total purchases where hour == 11
total_hour_11 = df.loc[df["hour"] == 11, "total"].sum()

print("Total purchases during hour 11:", total_hour_11)