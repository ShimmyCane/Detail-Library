import sqlite3
import json
import os

DB_PATH = "data/db/details.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            project TEXT,
            category TEXT,
            tags TEXT,
            description TEXT,
            metadata TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_detail(filename, project, category, tags, description, metadata):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO details (filename, project, category, tags, description, metadata)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (filename, project, category, json.dumps(tags), description, json.dumps(metadata)))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
