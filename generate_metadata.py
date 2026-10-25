from pathlib import Path
import json
import os
import shutil
from datetime import datetime

# Set base directory to the folder containing this script
BASE_DIR = Path(__file__).resolve().parent
IMAGES_ROOT = BASE_DIR / "images"
RAW_IMAGES_DIR = IMAGES_ROOT / "raw"
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
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            try:
                db = {item['filename']: item for item in json.load(f)}
            except json.JSONDecodeError:
                db = {}
    else:
        db = {}
            
    # Ensure raw directory exists
    RAW_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Scan ONLY the raw images folder for new entries
    for path in RAW_IMAGES_DIR.rglob('*'):
        if path.suffix.lower() in ('.png', '.jpg', '.jpeg'):
            # Get path relative to 'images/' folder
            rel_path = str(path.relative_to(IMAGES_ROOT)).replace('\\', '/')

            # Extract folder name as a potential tag (excluding 'raw')
            folder_name = path.parent.name
            initial_tags = []
            if folder_name not in ["raw", "images"]:
                initial_tags.append(folder_name)

            if rel_path not in db:
                print(f"New image found in raw: {rel_path}")
                db[rel_path] = {
                    "filename": rel_path,
                    "description": "Pending AI description...",
                    "tags": initial_tags,
                    "status": "new" 
                }
            else:
                # If already exists but moved/found again, update status if needed
                # (Optional: sync tags if folder changed)
                if folder_name not in ["raw", "images"] and folder_name not in db[rel_path].get('tags', []):
                    db[rel_path].setdefault('tags', []).append(folder_name)
                    if db[rel_path].get('status') == 'reviewed':
                        db[rel_path]['status'] = "needs_review"

    # Save back to list format
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(db.values()), f, indent=2)
    print("Database updated.")

if __name__ == "__main__":
    backup_db()
    update_db()

