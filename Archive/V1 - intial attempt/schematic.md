# TASK SPECIFICATION: Offline Local PNG Detail Library MVP (Manual-Tagging / Page-First)

Build a 100% offline local Desktop Web application using Python (Streamlit) and SQLite to catalog, manually tag, search, and visually review architectural/engineering details (stored as PNGs).

## 1. System Stack
- **Language**: Python 3.10+
- **Database**: `sqlite3` with `FTS5` (Full-Text Search enabled)
- **UI Framework**: Streamlit

## 2. Core Features & Data Flow

### A. Manual Ingestion & Tagging
1. User uploads/selects a PNG detail image.
2. Form fields pre-fill with persistent "last used" values (e.g., retaining current `Project Name`).
3. User enters/confirms:
   - `Project Name`
   - `Sheet Number` (e.g., A-501)
   - `Detail Number / Callout` (optional, e.g., 04)
   - `Category` (e.g., Waterproofing, Curtain Wall)
   - `Tags` (comma-separated, e.g., aluminum, sill, flashing)
   - `Notes`
4. Detail record and image path are committed to SQLite.

### B. Search & Metadata Filtering
- Text search bar querying `FTS5` index over tags, notes, category, and project name.
- Dropdown filters for exact match on `Project Name`, `Sheet Number`, and `Category`.
- Detail cards display preview images with provenance badges:
  `[Project Name] | Sheet: [Sheet #] | Detail: [Detail #]`

### C. Project Review Board
- Action button on each search result card: **"Add to Project Canvas"**.
- Dedicated "Project Board" tab displays a responsive grid of pinned details.
- Each pinned card includes quick-action buttons:
  - "Copy File Path"
  - "Copy Image to Clipboard"
  - "Remove from Board"

---

## 3. Directory Structure

```
.
├── app.py                   # Streamlit UI entrypoint
├── requirements.txt         # Dependencies
├── core/
│   └── db_manager.py        # SQLite schema, FTS5 setup, and CRUD operations
└── storage/                 # Local data folder
    ├── library.db           # SQLite database file
    └── images/              # Source PNG detail images
```

## 4. Code Deliverables Needed

### Deliverable 1: `requirements.txt`
```text
streamlit>=1.30.0
```

### Deliverable 2: `core/db_manager.py`

Create a database manager with the following schema:

* **Table `projects`**: `id`, `name`, `created_at`
* **Table `details`**: `id`, `project_id`, `sheet_number`, `detail_number`, `title`, `category`, `tags`, `notes`, `image_path`, `created_at`
* **Virtual Table `details_fts`**: FTS5 table indexing `title`, `category`, `tags`, and `notes`.
* **Table `canvas`**: `id`, `detail_id`, `created_at`

### Deliverable 3: `app.py`

Build a 3-tab Streamlit dashboard:

* **Tab 1: Ingest & Tag**: Single-page uploader, preview pane, sticky input fields for fast tagging, and a "Save Detail" button.
* **Tab 2: Search Library**: Search bar and metadata filters outputting detail cards with provenance badges and "Add to Canvas" buttons.
* **Tab 3: Project Canvas**: Grid layout of pinned details with quick-copy path buttons.
