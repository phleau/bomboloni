import streamlit as st
import pandas as pd

# Initialize data storage
if "rsvp_data" not in st.session_state:
    st.session_state.rsvp_data = []

if "baking_votes" not in st.session_state:
    st.session_state.baking_votes = {}

# Title and description
st.title("Flo 3.O Bomboloni & Bubbles 🎉🍾")
st.write("Hi friends! Hope to see you this Saturday between 13:00-16:00.")
st.write("Please let me know if you're coming, tell me what *30* means to you, and drop your baking request below!")

# Input Fields
name = st.text_input("Your Name", key="name_input")
meaning_of_30 = st.text_area("What does 30 mean to you?", key="meaning_input")
baking_request = st.text_input("Your Baking Request", key="baking_input")

# Save RSVP when all fields are filled
if name and meaning_of_30 and baking_request:
    new_entry = {
        "Name": name,
        "What 30 Means": meaning_of_30,
        "Baking Request": baking_request,
    }
    if new_entry not in st.session_state.rsvp_data:  # Prevent duplicates
        st.session_state.rsvp_data.append(new_entry)
        if baking_request not in st.session_state.baking_votes:
            st.session_state.baking_votes[baking_request] = 0  # Initialize votes
        st.success(f"Thanks, {name}! Your RSVP is recorded.")

# Display Guest List
st.header("Who's Coming? 🧁")
if st.session_state.rsvp_data:
    df = pd.DataFrame(st.session_state.rsvp_data)
    st.table(df)
else:
    st.write("No RSVPs yet. Be the first!")

# Display Baking Requests with Voting
st.header("Baking Requests 🍩")
if st.session_state.baking_votes:
    for request, votes in st.session_state.baking_votes.items():
        col1, col2 = st.columns([4, 1])
        col1.write(f"**{request}**")
        if col2.button(f"Vote ({votes})", key=request):
            st.session_state.baking_votes[request] += 1
else:
    st.write("No baking requests yet. Add yours above!")

# Optional Extras: Event Countdown
st.sidebar.header("Countdown ⏳")
st.sidebar.write("The party starts this Saturday at 13:00. Get ready for bomboloni & bubbles!")
