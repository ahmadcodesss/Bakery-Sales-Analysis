import pandas as pd

# Load the Data sheet
df = pd.read_excel("bakery.xlsx", sheet_name="Data")

# Sum of 'total' for each hour (this is the SUMIF equivalent, repeated for all hours)
hourly_totals = df.groupby("hour")["total"].sum().sort_index()

print(hourly_totals) 