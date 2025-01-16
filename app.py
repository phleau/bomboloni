import streamlit as st
import pandas as pd
import os

# File to store data
DATA_FILE = "rsvp_data.csv"

# Function to load data
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Name", "What 30 Means", "Baking Request", "Votes"])

# Function to save data
def save_data(dataframe):
    dataframe.to_csv(DATA_FILE, index=False)

# Load data from file
rsvp_data = load_data()

# Title and description
st.title("Flo 3.O Bomboloni & Bubbles 🎉🍾")
st.write("Hi friends! Hope to see you this Saturday!")
st.write("Please let me know if you're coming, tell me what *30* means to you, and drop your baking request below!")

# Input Fields
name = st.text_input("Your Name")
meaning_of_30 = st.text_area("What does 30 mean to you?")
baking_request = st.text_input("Your Baking Request")

# Save RSVP when all fields are filled
if st.button("Submit") and name and meaning_of_30 and baking_request:
    new_entry = {
        "Name": name,
        "What 30 Means": meaning_of_30,
        "Baking Request": baking_request,
        "Votes": 0
    }
    rsvp_data = rsvp_data.append(new_entry, ignore_index=True)
    save_data(rsvp_data)
    st.success(f"Thanks, {name}! Your RSVP is recorded.")

# Display Guest List
st.header("Who's Coming? 🧁")
if not rsvp_data.empty:
    st.table(rsvp_data[["Name", "What 30 Means", "Baking Request"]])
else:
    st.write("No RSVPs yet. Be the first!")

# Voting on Baking Requests
st.header("Baking Requests 🍩")
if not rsvp_data.empty:
    for i, row in rsvp_data.iterrows():
        col1, col2 = st.columns([4, 1])
        col1.write(f"**{row['Baking Request']}**")
        if col2.button(f"Vote ({row['Votes']})", key=row["Baking Request"]):
            rsvp_data.at[i, "Votes"] += 1
            save_data(rsvp_data)
            st.experimental_rerun()
else:
    st.write("No baking requests yet. Add yours above!")

st.sidebar.write("WHEN?")
st.sidebar.write("This Saturday between 13-16h")
st.sidebar.write("WHERE?")
st.sidebar.write("2e Sweelinckstraat 133")
st.sidebar.write("WHAT TO BRING?")
st.sidebar.write("Yourself! No gifts needed, but if you really want to, bring an ingredient or flavour you'd love to see in the next Bekkerings Bakery! (orr coffee ;)")
