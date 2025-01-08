import streamlit as st

# List of all questions (you can extend this list with more if needed)
questions = [
    "What is your dog’s name?", "What breed is your dog?", "How old is your dog?", 
    "What is your dog’s weight?", "What color is your dog?", "Does your dog have a microchip?", 
    "Is your dog spayed or neutered?", "When and where did you adopt your dog?",
    "Who is your dog's veterinarian?", "What is your vet’s phone number?", 
    "What is the address of your vet’s office?", "Do you have an emergency vet contact?", 
    "Does your dog have any medical conditions or allergies?", "Does your dog take any medications?", 
    "When was your dog last vaccinated?", "When is your dog due for their next vaccination?", 
    "What brand/type of food does your dog eat?", "What is the portion size for each meal?", 
    "How many times a day does your dog eat?", "Does your dog eat any treats or snacks?", 
    "How often do you refill your dog’s water bowl?", "What is your dog’s usual walk routine?", 
    "What are your dog’s favorite walk locations?", "What type of walking equipment do you use?", 
    "Does your dog pull on the leash?", "Is your dog calm during walks?", 
    "Does your dog get distracted easily during walks?", "Does your dog have any walking-related issues?", 
    "How often do you bathe your dog?", "How often do you brush your dog?", "How often do you trim your dog’s nails?", 
    "How often do you clean your dog’s ears?", "Do you brush your dog’s teeth?", 
    "Does your dog need any special grooming care?", "What are your dog’s favorite toys or activities?", 
    "What are your dog’s fears or anxiety triggers?", "What commands does your dog know?", 
    "Does your dog have any behavioral issues?", "Is your dog good with other dogs?", 
    "Is your dog good with children?", "Is your dog good with strangers?", "What training goals are you working on?", 
    "What progress or challenges have you encountered in training?", "What methods are you using for training?", 
    "Does your dog see a trainer or attend any obedience classes?", "What is your dog’s daily routine?", 
    "Does your dog travel with you?", "Does your dog get car sick?", "Do you have a pet sitter or dog walker?", 
    "Does your dog need special instructions for sitters/walkers?", "Who are your emergency contacts?", 
    "What is your vet's emergency contact info?", "What is the contact info for your local pet poison control hotline?", 
    "What are your dog’s favorite toys or items?", "Are there any important dates related to your dog?"
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
    
    # Display the bingo board with text inputs and grid lines using Markdown and HTML
    bingo_completed = False
    board_html = '<table style="border-collapse: collapse; width: 100%;">'
    
    for i in range(5):
        board_html += '<tr>'
        for j in range(5):
            question = bingo_board[i][j]
            answer = st.text_input(question, key=f"q{i}{j}", value=st.session_state.answers[i][j], label_visibility="collapsed")
            
            # Update the answers in session state
            if answer != st.session_state.answers[i][j]:
                st.session_state.answers[i][j] = answer

            # Check if the question has been answered and add a checkmark or cross icon
            answered_status = "✔️" if answer else "❓"
            
            # Create a cell with border and padding
            board_html += f'<td style="border: 1px solid black; padding: 8px; text-align: center;">'
            board_html += f'<div>{question}</div>'
            board_html += f'<div>{answered_status}</div>'
            board_html += '</td>'
        board_html += '</tr>'
    
    board_html += '</table>'
    
    # Display the bingo board using Markdown to support HTML
    st.markdown(board_html, unsafe_allow_html=True)
    
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