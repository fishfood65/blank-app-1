import streamlit as st
import csv
import io
import pandas as pd

# List of updated questions (remove the first 7 questions, starting from the 8th question)
questions = [
    "🐕 Dog's Name", "🏥 Vet Contact Info (Name, Phone Number, Address)", "🥣 Describe the brand/type of food your dog eats", "🧳 Walk Routine (Time, Duration, Location, Behavior)", "🛁 Bathing Schedule", "🧸 Favorite Toys", "🎯 Current Training Goals",
    "🦴 Name the Breed", "⛑️ Emergency Vet Contact Info (Name, Phone Number, Address)", "🍖 Describe the portion size for each meal", "📍 Favorite Walk Location", "💈 Brushing Schedule", "🐶 Play Styles", "🥁 Training Progress/Challenges",
    "🎂 Dog’s Age and Weight", "💊 List all medical conditions or allergies", "🕥 Feeding Schedule", "🐶 Walking Equipment", "💅 Nail Trimming", "🎾 Favorite Activities", "📚 Training Methods", "🔖 Dog’s microchip number", "🕥 Medication Schedule with Dosage",
    "🍗 Name your dog’s treats or snacks", "🐾 Walk Behavior", "👂 Ear Cleaning", "❗ Fear/Anxiety Triggers", "🏫 Trainer Contact (Name, Phone, Email)", "🖼️ Describe the Dog’s Appearance from Memory", "💊 Medication Delivery Instructions", "🕥 How often do you give your dog treats or snacks",
    "🍭 Treats for Walk", "🦷 Teeth Brushing", "📢 Commands Known", "🌴 Travel carte or car travel setup", "✂️ Dog is Spayed or Neutered", "🗄️ Health & Vaccination History", "💧 Water bowl refill schedule", "💤 Sleep Schedule", "🌟 Special Grooming Needs",
    "🔍 Behavioral Issues", "🚗 Car Sickness?", "🏘️ Place and date the Dog was adopted", "📆 Date of Dog’s next check-up or vaccination", "Bonus: Special Instructions for Sitters/Walkers", "🎾 Special Activities or Playtimes", "🚶‍♂️ Bonus: Pet Walker Contact Info",
    "🐶 Socialization with other dogs, children, and strangers", "🏠 Bonus: Pet Sitter Contact Info"
]

# Store the questions in session state only once
if 'questions' not in st.session_state:
    st.session_state.questions = questions

# Initialize the session state for answers (Now 7 rows x 7 columns)
if 'answers' not in st.session_state:
    st.session_state.answers = [['' for _ in range(7)] for _ in range(7)]  # 7 rows x 7 columns

# Function to create the bingo board with text inputs and a header row
def create_bingo_board():
    # Create an empty board (7x7)
    bingo_board = [st.session_state.questions[i:i + 7] for i in range(0, 49, 7)]  # 49 questions, 7 per row

    # Define the header for the bingo board (could be "B", "I", "N", "G", "O", etc.)
    header = ['B', 'I', 'N', 'G', 'O', 'X', 'Y']

    # Prepare the data to populate the table (7x7 grid of answers)
    table_data = []

    # Fill the table data with text input elements for answers
    for i in range(7):  # 7 rows
        row = []
        for j in range(7):  # 7 columns in each row
            question = bingo_board[i][j]  # Get the question for this cell
            # Create a label showing the question and a text input to capture the answer
            with st.beta_expander(question, expanded=False):  # Makes it collapsible
                answer = st.text_input("Your Answer", key=f"q{i}{j}", value=st.session_state.answers[i][j])
                
                # Store the answer in session state if it changes
                if answer != st.session_state.answers[i][j]:
                    st.session_state.answers[i][j] = answer
                
                # Append the answer to the row (for creating the table later)
                row.append(f"{question}: {answer}")
        table_data.append(row)

    # Create a Pandas DataFrame to display the bingo board as a table
    df_bingo = pd.DataFrame(table_data, columns=header)

    # Display the table
    st.write("### Bingo Board", df_bingo)

    # After each user input, check for Bingo (row, colum