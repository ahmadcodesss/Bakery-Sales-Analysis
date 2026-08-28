import pandas as pd

# Load the Data sheet
df = pd.read_excel("bakery.xlsx", sheet_name="Data")

# Food item columns only (excludes beverages: americano, caffe latte, milk tea, lemon ade, vanila latte, berry ade)
food_items = [
    "angbutter", "plain bread", "jam", "croissant", "tiramisu croissant",
    "cacao deep", "pain au chocolat", "almond croissant", "croque monsieur",
    "mad garlic", "gateau chocolat", "pandoro", "cheese cake", "orange pound",
    "wiener", "tiramisu", "merinque cookies"
]

food_totals = df[food_items].sum()
print(food_totals)