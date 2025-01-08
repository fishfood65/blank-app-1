import streamlit as st
import csv
import io

# List of questions (questions or actions) with icons
questions = [
    "🐾 Task", "🐾 Task", "🐾 Task", "🐾 Task", "🐾 Task",
    "🐕 Dog's Name", "🏥 Vet Contact Info", "🐾 Favorite Walk Locations", "🧳 Emergency Vet Contact", "🍖 Feeding Schedule",
    "🦴 Medical Conditions/Allergies", "🧼 Grooming Schedule", "🐕 Commands Known", "🐕 Behavioral Issues", "🚶‍♂️ Walk Routine",
    "🍏 Favorite Treats", "🐾 Special Training Notes", "🐕 Daily Routine", "🐶 Dog’s Birthdate", "🐶 Health & Vaccination History",
    "💧 Water Bowl Refill Frequency", "🐕 Socialization with Other Dogs", "🐕 Behavioral Goals", "🧸 Favorite Toys", "🏠 Pet Sitter Contact Info",
    "📅 Next Vet Appointment", "🎾 Exercise & Playtime Preferences", "💊 Medication Schedule", "🐕 Dog’s Weight", "📞 Emergency Contact 1"
]

# Store the questions in session state only once
if 'questions' not in st.session_state:
    st.session_state.questions = questions

# Initialize the session state for answers
if 'answers' not in st.session_state:
    st.session_state.answers = [['' for _ in range(5)] for _ in range(5)]

# Function to create the bingo board with text inputs
def create_bingo_board():
    # Create an empty board (5x5)
    bingo_board = [st.session_state.questions[i:i + 5] for i in range(0, 25, 5)]

    bingo_completed = False

    # Create the bingo board in a simple list format without grid styling
    for i in range(5):
        cols = st.columns(5)  # Create 5 columns for each row of the board
        for j in range(5):
            question = bingo_board[i][j]
            with cols[j]:
                # Use a text input to capture the answer for each question
                answer = st.text_input(question, key=f"q{i}{j}", value=st.session_state.answers[i][j])
                # Store the answer in session state
                if answer != st.session_state.answers[i][j]:
                    st.session_state.answers[i][j] = answer

                # Display whether the question has been answered
                if answer:
                    st.write("✔️ Answered")
                else:
                    st.write("❓ Not Answered")

    # After each user input, check for Bingo (row, column, or diagonal completion)
    bingo_completed = check_bingo(st.session_state.answers)

    if bingo_completed:
        st.success("🎉 Bingo! You've completed a row, column, or diagonal!")
        # Show the download button after Bingo
        export_csv_button()

# Function to check for Bingo
def check_bingo(answers):
    # Check rows and columns for completeness
    for i in range(5):
        # Check row i
        if all(answers[i][j] != '' for j in range(5)):
            return True
        # Check column j
        if all(answers[j][i] != '' for j in range(5)):
            return True
    
    # Check diagonals
    if all(answers[i][i] != '' for i in range(5)):
        return True
    if all(answers[i][4-i] != '' for i in range(5)):
        return True
    
    return False

# Function to export answers to CSV
def export_csv_button():
    # Prepare the CSV data
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write the header (questions)
    writer.writerow(st.session_state.questions)
    
    # Write the answers
    for row in st.session_state.answers:
        writer.writerow(row)
    
    # Move to the beginning of the StringIO buffer
    output.seek(0)
    
    # Create a download button
    st.download_button(
        label="Download Answers as CSV",
        data=output.getvalue(),
        file_name="dog_care_bingo_answers.csv",
        mime="text/csv"
    )

# Title and description
st.title("Essential Dog Care Quiz - Bingo Board")
st.write("Complete the bingo board by answering questions about your dog's care. "
         "Enter your responses in the boxes below.")

# Call the function to display the board
create_bingo_board()