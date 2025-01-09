import streamlit as st
import csv
import io

# List of updated questions (49 questions in total)
questions = [
    "🐾 Basic Info", "🐾 Health and Medical", "🐾 Feeding Schedule", "🐾 Routine, Exercise and Walks", "🐾 Grooming and Hygiene",
    "🐾 Behavioral Notes", "🐾 Training Notes and Special Care", "🐕 Dog's Name", "🏥 Vet Contact Info (Name, Phone Number, Address)", "🥣 Describe the brand/type of food your dog eats",
    "🧳 Walk Routine (Time, Duration, Location, Behavior)", "🛁 Bathing Schedule", "🧸 Favorite Toys", "🎯 Current Training Goals", "🦴 Name the Breed",
    "⛑️ Emergency Vet Contact Info (Name, Phone Number, Address)", "🍖 Describe the portion size for each meal", "📍 Favorite Walk Location", "💈 Brushing Schedule", "🐶 Play Styles",
    "🥁 Training Progress/Challenges", "🎂 Dog’s Age and Weight", "💊 List all medical conditions or allergies", "🕥 Feeding Schedule", "🐶 Walking Equipment",
    "💅 Nail Trimming", "🎾 Favorite Activities", "📚 Training Methods", "🔖 Dog’s microchip number", "🕥 Medication Schedule with Dosage",
    "🍗 Name your dog’s treats or snacks", "🐾 Walk Behavior", "👂 Ear Cleaning", "❗ Fear/Anxiety Triggers", "🏫 Trainer Contact (Name, Phone, Email)",
    "🖼️ Describe the Dog’s Appearance from Memory", "💊 Medication Delivery Instructions", "🕥 How often do you give your dog treats or snacks", "🍭 Treats for Walk", "🦷 Teeth Brushing",
    "📢 Commands Known", "🌴 Travel carte or car travel setup", "✂️ Dog is Spayed or Neutered", "🗄️ Health & Vaccination History", "💧 Water bowl refill schedule",
    "💤 Sleep Schedule", "🌟 Special Grooming Needs", "🔍 Behavioral Issues", "🚗 Car Sickness?", "🏘️ Place and date the Dog was adopted",
    "📆 Date of Dog’s next check-up or vaccination", "Bonus: Special Instructions for Sitters/Walkers", "🎾 Special Activities or Playtimes", "🚶‍♂️ Bonus: Pet Walker Contact Info",
    "🐶 Socialization with other dogs, children, and strangers", "🏠 Bonus: Pet Sitter Contact Info"
]

# Store the questions in session state only once
if 'questions' not in st.session_state:
    st.session_state.questions = questions

# Initialize the session state for answers
if 'answers' not in st.session_state:
    st.session_state.answers = [['' for _ in range(7)] for _ in range(7)]  # 7x7 grid

# Function to create the bingo board with text inputs
def create_bingo_board():
    # Create an empty board (7x7)
    bingo_board = [st.session_state.questions[i:i + 7] for i in range(0, 49, 7)]  # Update to handle 49 questions

    bingo_completed = False

    # First, display the header row with questions, no input fields
    cols = st.columns(7)  # Create 7 columns for the header
    for j in range(7):
        with cols[j]:
            st.write(f"**{bingo_board[0][j]}**")  # Display question as header, no input field

    # Now create the remaining rows with input fields
    for i in range(1, 7):  # Start from row 1 (the second row, since row 0 is the header)
        cols = st.columns(7)  # Create 7 columns for each row of the board
        for j in range(7):
            question = bingo_board[i][j]
            with cols[j]:
                # Use a text input to capture the answer for each question (only for non-header rows)
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
    for i in range(7):
        # Check row i
        if all(answers[i][j] != '' for j in range(7)):
            return True
        # Check column j
        if all(answers[j][i] != '' for j in range(7)):
            return True
    
    # Check diagonals
    if all(answers[i][i] != '' for i in range(7)):
        return True
    if all(answers[i][6-i] != '' for i in range(7)):
        return True
    
    return False

# Function to export answers to CSV with questions and corresponding answers
def export_csv_button():
    # Prepare the CSV data
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write the header row (questions as the first column)
    writer.writerow(["Question", "Answer"])
    
    # Write each question and its corresponding answer in the rows
    for i in range(7):  # Update to 7 rows
        for j in range(7):  # 7 columns
            question = st.session_state.questions[i * 7 + j]  # Get the correct question from the list
            answer = st.session_state.answers[i][j]  # Get the corresponding answer

            # Write the question and its corresponding answer
            writer.writerow([question, answer])
    
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