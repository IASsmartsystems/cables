import pandas as pd
import json

excel_file = "PLANT MACHINES.xlsx"   # change if needed
output_file = "equipment_data.js"

# Load Excel
df = pd.read_excel(excel_file, header=0)

# First column = equipment
equipment_column = df.columns[0]
attributes = df.columns[1:]

result = {}

for _, row in df.iterrows():
    equipment = str(row[equipment_column]).strip()

    # Skip empty equipment rows
    if equipment.lower() == "nan" or equipment == "":
        continue

    result[equipment] = {}

    for attr in attributes:
        value = row[attr]

        if pd.isna(value):
            continue

        # Convert cell like "12, 18, 22" into list
        pages = [p.strip() for p in str(value).split(",") if p.strip()]

        if pages:
            result[equipment][attr] = pages

# Write to JS file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const EQUIPMENT_DATA = ")
    json.dump(result, f, indent=2)
    f.write(";")

print("Done! Created equipment_data.js")
