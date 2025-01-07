import streamlit as st
import pandas as pd
import os

# Title for the Streamlit app
st.title("Save Text Input Example")

# Text input field
user_input = st.text_area("Enter some text here:")

# Button to save the input data
if st.button("Save Data"):
    # Check if the user has entered any text
    if user_input:
        # Prepare the data to save (here we store it as a DataFrame)
        data = {"Input Data": [user_input]}
        
        # Check if the file exists
        file_path = "user_input_data.csv"
        
        if os.path.exists(file_path):
            # Append new data if the file already exists
            df = pd.read_csv(file_path)
            new_data = pd.DataFrame(data)
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(file_path, index=False)
        else:
            # Create a new CSV file and save the first input
            df = pd.DataFrame(data)
            df.to_csv(file_path, index=False)
        
        # Notify the user
        st.success("Data saved successfully!")
    else:
        st.warning("Please enter some text before clicking 'Save Data'.")

# Display saved data (optional)
if os.path.exists(file_path):
    st.subheader("Saved Data:")
    saved_data = pd.read_csv(file_path)
    st.write(saved_data)