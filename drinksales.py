import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("bakery.xlsx", sheet_name="Data")

drinks = ["americano", "caffe latte", "milk tea", "lemon ade", "vanila latte", "berry ade"]
drink_totals = df[drinks].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(drink_totals.index, drink_totals.values, color="darkcyan")

plt.title("Number of Sales per Drink Item")
plt.xlabel("Drink Item")
plt.ylabel("Units Sold")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()