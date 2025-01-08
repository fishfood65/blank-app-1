import streamlit as st

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

# Function to create the bingo board with text inputs
def create_bingo_board():
    # Create an empty board (5x5)
    bingo_board = [st.session_state.questions[i:i + 5] for i in range(0, 25, 5)]
    
    # Initialize session state for answers and completion tracking
    if 'answers' not in st.session_state:
        st.session_state.answers = [['' for _ in range(5)] for _ in range(5)]
    
    # HTML grid layout with a grid-template
    html_grid_layout = """
    <style>
    .bingo-board {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        padding: 10px;
    }
    .bingo-board div {
        border: 1px solid #ccc;
        padding: 20px;
        font-size: 16px;
        text-align: center;
        height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .task-text {
        margin-bottom: 10px;
        font-weight: bold;
    }
    .input-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """
    
    # Display HTML grid layout
    st.markdown(html_grid_layout, unsafe_allow_html=True)

    # Initialize a variable to check for Bingo completion
    bingo_completed = False

    # Create the bingo grid in HTML using div elements
    bingo_board_html = '<div class="bingo-board">'

    for i in range(5):
        for j in range(5):
            question = bingo_board[i][j]
            answer = st.text_input(question, key=f"q{i}{j}", value=st.session_state.answers[i][j])
            
            # Store the answer in session state
            if answer != st.session_state.answers[i][j]:
                st.session_state.answers[i][j] = answer
            
            # Append the HTML for each cell in the grid
            bingo_board_html += f'''
            <div>
                <div class="task-text">{question}</div>
                <div class="input-container">{answer}</div>
            </div>
            '''

    bingo_board_html += '</div>'

    # Display the HTML grid layout
    st.markdown(bingo_board_html, unsafe_allow_html=True)

    # After each user input, check for Bingo (row, column, or diagonal completion)
    bingo_completed = check_bingo(st.session_state.answers)
    
    if bingo_completed:
        st.success("🎉 Bingo! You've completed a row, column, or diagonal!")

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

# Title and description
st.title("Essential Dog Care Quiz - Bingo Board")
st.write("Complete the bingo board by answering questions about your dog's care. "
         "Enter your responses in the boxes below.")

# Call the function to display the board
create_bingo_board()