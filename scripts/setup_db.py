import sqlite3
import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

SCHEMA_PATH = "lib/db/schema.sql"
DB_PATH = "db/development.db"

def setup_schema():
    if not os.path.exists(SCHEMA_PATH):
        print("Schema file not found.")
        return

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    print(f"Schema created at {DB_PATH}")


def seed_database():
    from lib.db.seed import seed_data
    seed_data()

if __name__ == "__main__":
    setup_schema()
    seed_database()
    print("Database setup complete.")
