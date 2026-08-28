import pandas as pd

# Load the Data sheet
df = pd.read_excel("bakery.xlsx", sheet_name="Data")

# Total income per day of week
daily_totals = df.groupby("day of week")["total"].sum()

# Optional: put days in proper order (Mon–Sun) instead of alphabetical/random
day_order = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
daily_totals = daily_totals.reindex(day_order)

print(daily_totals)