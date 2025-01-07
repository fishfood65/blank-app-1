import streamlit as st
import pandas as pd
import os

# Title for the Streamlit app
st.title("Icon Click Input and Save")

# Display an icon using markdown with HTML
st.markdown("""
    <style>
    .icon { font-size: 50px; cursor: pointer; }
    </style>
    <div class="icon" id="icon">&#9993;</div>  <!-- Envelope icon -->
    <p>Click on the icon to enter your data.</p>
""", unsafe_allow_html=True)

# Flag to track if the icon was clicked
if 'icon_clicked' not in st.session_state:
    st.session_state.icon_clicked = False

# Function to handle icon click
def handle_icon_click():
    st.session_state.icon_clicked = True

# Button for icon click
if st.button("Click the icon to enter data"):
    handle_icon_click()

# Input field that appears after icon click
if st.session_state.icon_clicked:
    # Ask for user input after icon click
    user_input = st.text_area("Enter your text here:")

    # Button to submit and save the input data
    if st.button("Save Data"):
        # Check if the user has entered any text
        if user_input:
            # Prepare data for saving
            data = {"Input Data": [user_input]}
            
            # Define file path
            file_path = "user_input_data.csv"
            
            if os.path.exists(file_path):
                # Append data to the existing file
                df = pd.read_csv(file_path)
                new_data = pd.DataFrame(data)
                df = pd.concat([df, new_data], ignore_index=True)
                df.to_csv(file_path, index=False)
            else:
                # Create a new CSV file and save the first input
                df = pd.DataFrame(data)
                df.to_csv(file_path, index=False)
            
            # Notify user
            st.success("Data saved successfully!")
        else:
            st.warning("Please enter some text before clicking 'Save Data'.")

# Optional: Display saved data
if os.path.exists("user_input_data.csv"):
    st.subheader("Saved Data:")
    saved_data = pd.read_csv("user_input_data.csv")
    st.write(saved_data)