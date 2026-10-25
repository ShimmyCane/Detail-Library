import sqlite3
import json

def get_all_details():
    conn = sqlite3.connect("data/db/details.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM details")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "filename": row[1],
            "project": row[2],
            "category": row[3],
            "tags": json.loads(row[4]),
            "description": row[5],
            "metadata": json.loads(row[6])
        }
        for row in rows
    ]
