# setup_db.py: Initializes and seeds the database

import sqlite3
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

SCHEMA_PATH = "lib/db/schema.sql"
DB_PATH = "db/development.db"  # Changed to match connection.py

# Step 1: Create schema
def setup_schema():
    if not os.path.exists(SCHEMA_PATH):
        print("Schema file not found.")
        return

    # Create db directory if it doesn't exist
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    print(f"Schema created at {DB_PATH}")

# Step 2: Seed data
def seed_database():
    from lib.db.seed import seed_data
    seed_data()

if __name__ == "__main__":
    setup_schema()
    seed_database()
    print("Database setup complete.")
    