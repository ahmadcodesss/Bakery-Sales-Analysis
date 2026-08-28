import pandas as pd
import matplotlib.pyplot as plt

# Load the Data sheet
df = pd.read_excel("bakery.xlsx", sheet_name="Data")

# Food item columns only (excludes beverages)
food_items = [
    "angbutter", "plain bread", "jam", "croissant", "tiramisu croissant",
    "cacao deep", "pain au chocolat", "almond croissant", "croque monsieur",
    "mad garlic", "gateau chocolat", "pandoro", "cheese cake", "orange pound",
    "wiener", "tiramisu", "merinque cookies"
]

food_totals = df[food_items].sum().sort_values(ascending=False)

# Bar chart
plt.figure(figsize=(12, 6))
plt.bar(food_totals.index, food_totals.values, color="peru")

plt.title("Number of Sales per Food Item")
plt.xlabel("Food Item")
plt.ylabel("Units Sold")

plt.xticks(rotation=45, ha="right")  # rotate labels so they don't overlap
plt.tight_layout()
plt.show()