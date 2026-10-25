import sqlite3
import os
from datetime import datetime

# Updated path to reflect the new structure
DB_PATH = "storage/library.db"

def get_connection():
    # Ensure the storage directory exists before connecting
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tables
    cursor.execute("CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT UNIQUE, created_at TIMESTAMP)")
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS details (
            id INTEGER PRIMARY KEY, 
            project_id INTEGER,
            sheet_number TEXT, 
            detail_number TEXT, 
            title TEXT, 
            category TEXT, 
            tags TEXT, 
            notes TEXT, 
            image_path TEXT, 
            created_at TIMESTAMP, 
            FOREIGN KEY(project_id) REFERENCES projects(id)
        )
    """)
    









    # FTS5 Table
    cursor.execute("CREATE VIRTUAL TABLE IF NOT EXISTS details_fts USING fts5(title, category, tags, notes, content='details', content_rowid='id')")
    
    # Canvas Table
    cursor.execute("CREATE TABLE IF NOT EXISTS canvas (id INTEGER PRIMARY KEY, detail_id INTEGER, created_at TIMESTAMP, FOREIGN KEY(detail_id) REFERENCES details(id))")

    conn.commit()
    conn.close()

# Initialize DB
init_db()

