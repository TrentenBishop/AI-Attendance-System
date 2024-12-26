import streamlit as st
from threading import Thread
import subprocess

# Function to start the dataset recording in a separate thread
def start_dataset(name):
    subprocess.run(['python', 'Dataset.py'], input=name.encode())

# Function to start attendance tracking in a separate thread
def start_attendance():
    subprocess.run(['python', 'Attendance.py'])

# Streamlit UI components
st.title("AI Attendance System")

# Start dataset section
st.subheader("Start Dataset Recording")
name = st.text_input("Enter your name for dataset recording:")
if st.button("Start Dataset"):
    if name:
        st.write(f"Starting dataset recording for {name}...")
        # Run the dataset recording in a background thread
        Thread(target=start_dataset, args=(name,)).start()
    else:
        st.error("Please enter a name.")

# Start attendance section
st.subheader("Start Attendance Tracking")
if st.button("Start Attendance"):
    st.write("Starting attendance tracking...")
    # Run the attendance tracking in a background thread
    Thread(target=start_attendance).start()

