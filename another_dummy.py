import pandas as pd

# Example: Read your dataframe
df = pd.read_csv("D:/Multi Agent AI Governance System - Sample/healthcare_dataset.csv")  # or any other method to load the dataframe

# Convert 'Billing Amount' to 2 decimal places (in float)
df['Billing Amount'] = df['Billing Amount'].round(2)

# If you want it formatted as string with 2f (like '18856.28')
# df['Billing Amount'] = df['Billing Amount'].apply(lambda x: f"{x:.2f}")

# Save it back to CSV (optional)
df.to_csv("heatlcare_data.csv", index=False)