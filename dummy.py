import os

db_path = "governance.db"

if os.path.exists(db_path):
    os.remove(db_path)
    print("✅ Database deleted successfully.")
else:
    print("❌ Database file not found.")