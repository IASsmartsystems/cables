import pandas as pd
import json

# ===== CONFIG =====
EXCEL_FILE = "new machines.xlsx"      # your excel file
SHEET_NAME = 0                 # or "Sheet1"
OUTPUT_JS = "app_data.js"
# ==================

# Read Excel
df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)

# Replace NaN with empty strings
df = df.fillna("")

# Convert dataframe rows to list of dicts
records = df.to_dict(orient="records")

# Write JS file
with open(OUTPUT_JS, "w", encoding="utf-8") as f:
    f.write("const APP_DATA = ")
    json.dump(records, f, indent=2)
    f.write(";")

print(f"✅ {OUTPUT_JS} generated successfully!")
print(f"📄 Rows exported: {len(records)}")
