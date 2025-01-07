import streamlit as st
import pandas as pd
import random
import os

# Define the Bingo tasks with corresponding icons
tasks = [
    ("Dog's Name", "🐕"),
    ("Vet Contact Info", "📞"),
    ("Favorite Walk Locations", "🚶‍♂️"),
    ("Emergency Vet Contact", "🚑"),
    ("Feeding Schedule", "🍽️"),
    ("Medical Conditions/Allergies", "💊"),
    ("Grooming Schedule", "💇‍♂️"),
    ("Commands Known", "🎓"),
    ("Behavioral Issues", "📝"),
    ("Walk Routine", "🚶"),
    ("Favorite Treats", "🍖"),
    ("Special Training Notes", "📚"),
    ("Daily Routine", "📅"),
    ("Dog’s Birthdate", "🎂"),
    ("Health & Vaccination History", "💉"),
    ("Water Bowl Refill Frequency", "💧"),
    ("Socialization with Other Dogs", "🐶"),
    ("Behavioral Goals", "🎯"),
    ("Favorite Toys", "🧸"),
    ("Pet Sitter Contact Info", "📲"),
    ("Next Vet Appointment", "📅"),
    ("Exercise & Playtime Preferences", "⚽"),
    ("Medication Schedule", "💊"),
    ("Dog’s Weight", "⚖️"),
    ("Emergency Contact 1", "👨‍👩‍👧‍👦")
]

# Shuffle tasks and create a 5x5 Bingo board
random.shuffle(tasks)
bingo_board = pd.DataFrame([tasks[i:i + 5] for i in range(0, len(tasks), 5)], columns=[f"Col {i+1}" for i in range(5)])

# Data storage for completed tasks
completed_data = []

# Check if a CSV file exists to load previous data
if os.path.exists("completed_tasks.csv"):
    completed_data = pd.read_csv("completed_tasks.csv").to_dict(orient='records')

# Streamlit UI
st.title("Dog Care Bingo Board!")
st.write("Complete each task to fill out your essential dog care template. Track your progress by clicking a cell and entering details.")

# Display Bingo board in a table view with icons
def display_bingo_board(board, completed_data):
    board_html = "<table style='width:100%; border: 1px solid black; border-collapse: collapse;'>"
    for i, row in board.iterrows():
        board_html += "<tr>"
        for col in board.columns:
            task, icon = row[col]
            task_id = f"{task}_{col}_{i}"
            # Check if the task is completed by matching task_id in completed_data
            task_completed = any(task['task_id'] == task_id for task in completed_data)
            completion_text = "✔" if task_completed else ""
            board_html += f"<td style='padding: 10px; text-align: center; border: 1px solid black; cursor: pointer;' onclick='st.session_state.cell_clicked = \"{task_id}\"'>{task} {icon} {completion_text}</td>"
        board_html += "</tr>"
    board_html += "</table>"
    st.markdown(board_html, unsafe_allow_html=True)

# Call the function to display the Bingo board
display_bingo_board(bingo_board, completed_data)

# Form submission logic
if 'cell_clicked' in st.session_state:
    clicked_cell = st.session_state.cell_clicked
    task_name, col, row = clicked_cell.split("_")
    
    # Display form to enter task details
    with st.form(key='task_input_form'):
        user_input = st.text_input(f"Enter details for '{task_name}'")
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            if user_input:
                # Save the task as completed with the user input
                completed_data.append({"task_id": clicked_cell, "task_name": task_name, "data": user_input})
                st.session_state.cell_clicked = None  # Clear the clicked task
                st.success(f"Task '{task_name}' completed!")
                st.experimental_rerun()  # Re-run to update the board

# Save the completed tasks to a CSV file
def save_data_to_csv(completed_data):
    if completed_data:
        df = pd.DataFrame(completed_data)
        df.to_csv("completed_tasks.csv", index=False)

# Save the data when the user leaves the app or refreshes
save_data_to_csv(completed_data)