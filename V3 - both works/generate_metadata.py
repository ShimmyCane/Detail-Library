from pathlib import Path
import json
import os
import shutil
from datetime import datetime

# Set base directory to the folder containing this script
BASE_DIR = Path(__file__).resolve().parent
IMAGES_ROOT = BASE_DIR / "images"
DB_FILE = BASE_DIR / "details.json"

def backup_db():
    if DB_FILE.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BASE_DIR / "data" / f"details_backup_{timestamp}.json"
        # Ensure data folder exists
        backup_path.parent.mkdir(exist_ok=True)
        shutil.copy(DB_FILE, backup_path)
        print(f"Backup created: {backup_path}")

def update_db():
    # Load existing DB
    if DB_FILE.exists():
            with open(DB_FILE, 'r') as f:
            db = {item['filename']: item for item in json.load(f)}
        else:
        db = {}
            
    # Scan all images recursively
    for path in IMAGES_ROOT.rglob('*'):
        if path.suffix.lower() in ('.png', '.jpg', '.jpeg'):
            # Get path relative to 'images/' folder
            rel_path = str(path.relative_to(IMAGES_ROOT)).replace('\\', '/')

            # Extract folder name as a potential tag
            folder_name = path.parent.name

            if rel_path not in db:
                print(f"New image found: {rel_path}")
                db[rel_path] = {
                    "filename": rel_path,
                    "description": "Pending AI description...",
                    "tags": [folder_name] if folder_name != "images" else [],
                    "status": "new" # Track status
                }
    else:
                # If moved, update folder tag and flag for review
                if folder_name != "images" and folder_name not in db[rel_path].get('tags', []):
                    db[rel_path].setdefault('tags', []).append(folder_name)
                    db[rel_path]['status'] = "needs_review"

    # Save back to list format
    with open(DB_FILE, 'w') as f:
        json.dump(list(db.values()), f, indent=2)
    print("Database updated.")

if __name__ == "__main__":
    backup_db()
    update_db()

