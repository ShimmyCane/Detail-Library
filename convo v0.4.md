# Convo v0.4 - Detail Library MVP
Path: 03 Projects/Detail Library


## Status
- [x] Simplified architecture (Static site: HTML + JSON + Images)
- [x] Folder structure, `generate_metadata.py` refactored (BASE_DIR)
- [x] Basic UI (`index.html`) + Arch Summary (`index_summary.html`)
- [x] Editor UI (`editor.html`) created for manual metadata population
- [x] Tag filtering and sorting implemented in `index.html`
## Next Steps
- [ ] Update `generate_metadata.py` to scan `images/raw/` instead of `images/`
- [ ] Add search functionality to `index.html` (Client-side search for now)
- [ ] Integrate LLM for tag generation (based on description)
- [ ] Implement local backend (optional) to make `editor.html` "Save" write directly to `details.json`
## Notes
- Workflow: `images/raw/` -> `generate_metadata.py` -> `editor.html` -> `details.json` -> Move to `images/`
- MVP excludes: Computer vision, OCR, CLIP, vector database, automatic detail detection.
- Focus: "Retrieve with structured metadata; understand with descriptions; rank with an LLM; trust the human."

