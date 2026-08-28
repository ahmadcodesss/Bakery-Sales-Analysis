import pandas as pd
import matplotlib.pyplot as plt

# Load the Data sheet
df = pd.read_excel("bakery.xlsx", sheet_name="Data")

food_items = [
    "angbutter", "plain bread", "jam", "croissant", "tiramisu croissant",
    "cacao deep", "pain au chocolat", "almond croissant", "croque monsieur",
    "mad garlic", "gateau chocolat", "pandoro", "cheese cake", "orange pound",
    "wiener", "tiramisu", "merinque cookies"
]
drink_items = ["americano", "caffe latte", "milk tea", "lemon ade", "vanila latte", "berry ade"]

df["food items"] = df[food_items].sum(axis=1)
df["drinks"] = df[drink_items].sum(axis=1)

summary = df.groupby("hour")[["food items", "drinks"]].sum().sort_index()
summary["% Food sales"] = (summary["food items"] / (summary["food items"] + summary["drinks"])) * 100
summary["% Drink sales"] = (summary["drinks"] / (summary["food items"] + summary["drinks"])) * 100

print(summary)

# Line chart
plt.figure(figsize=(10, 6))
plt.plot(summary.index, summary["food items"], marker="o", label="Food sales")
plt.plot(summary.index, summary["drinks"], marker="o", label="Drink Sales")

plt.title("Food and Drink Sales per Hour")
plt.xlabel("Hour")
plt.ylabel("Items Sold")
plt.xticks(summary.index)
plt.legend()
plt.tight_layout()
plt.show()

# 100% stacked column chart
plt.figure(figsize=(10, 6))
plt.bar(summary.index.astype(str), summary["% Food sales"], label="% Food sales", color="peru")
plt.bar(summary.index.astype(str), summary["% Drink sales"], bottom=summary["% Food sales"],
        label="% Drink sales", color="darkcyan")

plt.title("Proportion of Food vs Drink Sales per Hour")
plt.xlabel("Hour")
plt.ylabel("Proportion (%)")
plt.legend()
plt.tight_layout()
plt.show()