import json
import os
import base64

# This script will eventually use an LLM to generate metadata.
# For now, it just scans the images folder and creates a template entry for new images.

IMAGES_DIR = "images"
DB_FILE = "details.json"

def get_existing_filenames():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        data = json.load(f)
        return [item['filename'] for item in data]

def update_db():
    existing = get_existing_filenames()
    new_entries = []
    
    for filename in os.listdir(IMAGES_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')) and filename not in existing:
            print(f"New image found: {filename}")
            new_entries.append({
                "filename": filename,
                "description": "Pending AI description...",
                "tags": []
            })
            
    if new_entries:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                data = json.load(f)
        else:
            data = []
            
        data.extend(new_entries)
        
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Added {len(new_entries)} new entries to {DB_FILE}")
    else:
        print("No new images found.")

if __name__ == "__main__":
    update_db()
