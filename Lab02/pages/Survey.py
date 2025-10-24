# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).
import csv

# PAGE CONFIGURATION
st.set_page_config(
    page_title="MK1 Character Survey",
    page_icon="🔥",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("🔥 Mortal Kombat 1 Character Survey 🔥")
st.write("Tell us what you think about MK1 fighters! Fill out the form below and submit your answers.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    
    kameo_char = st.text_input("Strongest Kameo?")
    kombo_value = st.text_input("What is the highest percent combo you've done?")
    annoying_char = st.text_input("Who is the most annoying to fight?")
    skill_check = st.text_input("From 1-10 rate how good you think you are?")
    coolest_design = st.text_input("Who has the coolest design?")
    strongest_char = st.text_input("Best Character Overall?")

    submitted = st.form_submit_button("Submit Data")
    
    if submitted:
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.
        kameo_char = kameo_char.strip().title()
        annoying_char = annoying_char.strip().title()
        coolest_design = coolest_design.strip().title()
        strongest_char = strongest_char.strip().title()

        file_exists = os.path.exists("data.csv")
        
    
        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                "Strongest Kameo",
                "Highest Percent Combo",
                "Most Annoying Opponent",
                "Skill Rating",
                "Coolest Design",
                "Best Character Overall"
                ])
            
            writer.writerow([
                kameo_char, kombo_value,
                annoying_char, skill_check,
                coolest_design, strongest_char
            ])

        st.success("✅ Your MK1 survey data has been submitted!")
        st.write("### Your Responses")
        st.write(f"**Strongest Kameo:** {kameo_char}")
        st.write(f"**Highest Percent Combo:** {kombo_value}%")
        st.write(f"**Most Annoying Opponent:** {annoying_char}")
        st.write(f"**Skill Rating:** {skill_check}/10")
        st.write(f"**Coolest Design:** {coolest_design}")
        st.write(f"**Best Character Overall:** {strongest_char}")

# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
