import streamlit as st
import os
from datetime import datetime
from core.db_manager import init_db, get_connection

# Initialize
init_db()

st.set_page_config(page_title="PNG Detail Library", layout="wide")
st.title("🖼️ PNG Detail Library")

tabs = st.tabs(["Ingest & Tag", "Search Library", "Project Canvas"])

# --- Tab 1: Ingest & Tag ---
with tabs[0]:
    st.header("Ingest New Detail")
    uploaded_file = st.file_uploader("Upload PNG", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        # Save file to storage
        save_dir = "storage/images"
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.image(save_path, caption="Preview")

        with st.form("tagging_form"):
            project = st.text_input("Project Name")
            sheet = st.text_input("Sheet Number")
            detail = st.text_input("Detail Number")
            title = st.text_input("Title")
            category = st.text_input("Category")
            tags = st.text_input("Tags (comma separated)")
            notes = st.text_area("Notes")
            
            if st.form_submit_button("Save Detail"):
                st.write(f"Saving: {uploaded_file.name} to {save_path}")
                conn = get_connection()
                cursor = conn.cursor()
                
                # Ensure project exists
                cursor.execute("INSERT OR IGNORE INTO projects (name, created_at) VALUES (?, ?)", (project, datetime.now()))
                cursor.execute("SELECT id FROM projects WHERE name = ?", (project,))
                project_id = cursor.fetchone()[0]
                
                # Insert detail
                cursor.execute("""
                    INSERT INTO details (project_id, sheet_number, detail_number, title, category, tags, notes, image_path, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (project_id, sheet, detail, title, category, tags, notes, save_path, datetime.now()))
                
                conn.commit()
                conn.close()
                st.success("Detail saved!")

# --- Tab 2: Search Library ---
with tabs[1]:
    st.header("Search Library")
    query = st.text_input("Search details...")
    st.write("Search functionality coming soon.")

# --- Tab 3: Project Canvas ---
with tabs[2]:
    st.header("Project Canvas")
    st.write("Pinned details will appear here.")

