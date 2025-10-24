# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

try:
    if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
        data = pd.read_csv("data.csv")
        st.success("✅ CSV loaded successfully!")
        st.dataframe(data)  # NEW
    else:
        st.warning("⚠️ The 'data.csv' file is empty or missing.")
        data = None
except Exception as e:
    st.error(f"Error reading CSV file: {e}")
    data = None

try:
    with open("data.json", "r") as file:
        json_data = json.load(file)
        st.success("✅ JSON loaded successfully!")
        st.json(json_data)  # NEW
except Exception as e:
    st.error(f"Error reading JSON file: {e}")
    json_data = None


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Static - Fan Favorite Characters") 
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.

st.write("This static bar chart shows an example dataset of estimated fan favorites in Mortal Kombat 1.")
static_data = {
    "Character": ["Scorpion", "Sub-Zero", "Mileena", "Liu Kang", "Rain"],
    "Votes": [95, 90, 85, 80, 70]
}
static_df = pd.DataFrame(static_data)
st.bar_chart(static_df.set_index("Character")["Votes"])  # NEW


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Dynamic - Skill Ratings (from CSV)") 
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.

st.write("This bar chart shows players’ self-rated skill levels from the MK1 survey. Use the slider to filter ratings.")

if data is not None and "Skill Rating" in data.columns:
    # Convert to numeric if user entered text
    data["Skill Rating"] = pd.to_numeric(data["Skill Rating"], errors="coerce")

    # Interactive widget using session state
    if "min_skill" not in st.session_state:
        st.session_state.min_skill = 0

    st.session_state.min_skill = st.slider("Select minimum skill rating:", 0, 10, st.session_state.min_skill)  # NEW

    filtered_data = data[data["Skill Rating"] >= st.session_state.min_skill]

    # Display the dynamic bar chart
    st.bar_chart(filtered_data.set_index("Best Character Overall")["Skill Rating"])
else:
    st.warning("CSV file missing or missing 'Skill Rating' column.")


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Dynamic - Combo Percentages (from JSON)") 
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

st.write("This line chart displays combo percentages read from the JSON file. Use the multiselect to pick characters.")

if json_data and "data_points" in json_data:
    json_df = pd.DataFrame(json_data["data_points"])

    # Create multiselect using session state
    if "selected_chars" not in st.session_state:
        st.session_state.selected_chars = json_df["label"].tolist()

    st.session_state.selected_chars = st.multiselect(
        "Select which characters to display:",
        json_df["label"].tolist(),
        default=st.session_state.selected_chars  # NEW
    )

    filtered_json = json_df[json_df["label"].isin(st.session_state.selected_chars)]
    st.line_chart(filtered_json.set_index("label")["value"])
else:
    st.warning("⚠️ JSON data missing or invalid.")
