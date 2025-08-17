import pandas as pd
import re
import csv

# Define consistent column names (adjust if your file has different ones)
columns = ["Full Name", "Company Name", "Instagram URL", "Email Address", "Phone Number", "Extra"]

# Read CSV safely (handles rows with different numbers of fields)
rows = []
with open("houston_construction_leads.csv", "r", encoding="utf-8", errors="ignore") as f:
    reader = csv.reader(f)
    for row in reader:
        # Pad or trim each row to 6 columns
        if len(row) < len(columns):
            row.extend([""] * (len(columns) - len(row)))
        elif len(row) > len(columns):
            row = row[:len(columns)]
        rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows[1:], columns=columns)  # skip header row

# --- Email/Phone Fixing Functions ---
def is_email(value):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", str(value))) if value else False

def is_phone(value):
    return bool(re.match(r"^\+?\d[\d\s\-\(\)]{6,}$", str(value))) if value else False

# --- Fix Rows ---
for i, row in df.iterrows():
    email_val = row["Email Address"]
    phone_val = row["Phone Number"]
    extra_val = row["Extra"]

    # If email column has phone and phone has email → swap
    if is_phone(email_val) and is_email(phone_val):
        df.at[i, "Email Address"] = phone_val
        df.at[i, "Phone Number"] = email_val

    # If email missing/invalid → try recovering from phone or extra
    elif not is_email(email_val):
        if is_email(phone_val):
            df.at[i, "Email Address"] = phone_val
            df.at[i, "Phone Number"] = ""
        elif is_email(extra_val):
            df.at[i, "Email Address"] = extra_val
            df.at[i, "Extra"] = ""

# Save cleaned file
df.to_csv("houston_construction_leads_cleaned.csv", index=False, encoding="utf-8")
print("✅ Fixed file saved as 'houston_construction_leads_cleaned.csv'")
