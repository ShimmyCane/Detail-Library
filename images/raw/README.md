# images/raw

Staging area for the Detail Library. Nothing here is published until it is selected.

## Rules

- **Allowed licences:** `Public domain`, `CC0`, `CC BY`, `CC BY-SA`. Each file needs an entry in `licences.json` with its licence, credit and source. CC BY and CC BY-SA files need their credit kept with them. Anything else is not added.
- **Tagging:** the licence shows on each card in the library, and the library can filter by it.
- **Folders are categories.** `wall/masonry/` means the tags `wall` and `masonry`. Files directly in `raw/` have no tags.
- **Formats:** `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif` (raster), `.svg` (vector), `.pdf`.

## Workflow

1. Create the framework (the category folders are already here).
2. Source details into the matching folder, and record each file's licence in `licences.json`. Filter, tag and select.
3. Selected details leave this folder. Where they go next is not decided yet.
4. Push selected details to the Quick Detail cloud library.

`image-log.json` is written by the generator. It has one record per file: size, SHA-256, pixel size, licence, credit, source, and the first and last dates it was seen.

Run `python3 ../../generate_library.py` after changing files, then open `library.html` to browse them.
