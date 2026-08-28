import pandas as pd
import matplotlib.pyplot as plt

# Load the Data sheet
df = pd.read_excel("bakery.xlsx", sheet_name="Data")

# Total income per hour
hourly_totals = df.groupby("hour")["total"].sum().sort_index()

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(hourly_totals.index, hourly_totals.values, color="steelblue")

plt.title("Total Income per Business Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Total Income")

plt.xticks(hourly_totals.index)  # show every hour as a tick, not just some
plt.tight_layout()
plt.show()