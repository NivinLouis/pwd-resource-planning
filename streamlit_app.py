import streamlit as st

# --- PAGE SETUP ---
dashboard_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
    default=True
)
search_page = st.Page(
    page="views/search.py",
    title="Individual Data",
    icon=":material/person_search:"
)
database_page = st.Page(
    page="views/database.py",
    title="Database",
    icon=":material/view_list:"
)
add_page = st.Page(
    page="views/add.py",
    title="Add Person",
    icon=":material/person_add:"
)
import_page = st.Page(
    page="views/import.py",
    title="Import Data",
    icon=":material/publish:"
)
#recent_page = st.Page(page="views/recent.py",title="Recents",icon=":material/work_history:")
about_page = st.Page(
    page="views/about.py",
    title="About",
    icon=":material/info:"
)

# --- Navigation Setuo ---
pg=st.navigation(
    {
        "Home": [dashboard_page],
        "Data": [database_page,search_page],
        "Add Data": [add_page,import_page],
        "Help": [about_page]
    }
)
# --- Shared on all pages ---
st.logo("assets/logo.png")
#st.sidebar.text("Made by students of vidya")

# --- Run Navigation ---
pg.run()
