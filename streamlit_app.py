import streamlit as st

# List of tasks (questions or actions) with icons
tasks = [
    "🐾 Task", "🐾 Task", "🐾 Task", "🐾 Task", "🐾 Task",
    "🐕 Dog's Name", "🏥 Vet Contact Info", "🐾 Favorite Walk Locations", "🧳 Emergency Vet Contact", "🍖 Feeding Schedule",
    "🦴 Medical Conditions/Allergies", "🧼 Grooming Schedule", "🐕 Commands Known", "🐕 Behavioral Issues", "🚶‍♂️ Walk Routine",
    "🍏 Favorite Treats", "🐾 Special Training Notes", "🐕 Daily Routine", "🐶 Dog’s Birthdate", "🐶 Health & Vaccination History",
    "💧 Water Bowl Refill Frequency", "🐕 Socialization with Other Dogs", "🐕 Behavioral Goals", "🧸 Favorite Toys", "🏠 Pet Sitter Contact Info",
    "📅 Next Vet Appointment", "🎾 Exercise & Playtime Preferences", "💊 Medication Schedule", "🐕 Dog’s Weight", "📞 Emergency Contact 1"
]

# Create the bingo board with text inputs
def create_bingo_board():
    # Initialize session state for storing responses if not present
    if 'responses' not in st.session_state:
        st.session_state.responses = {f"q{i}{j}": "" for i in range(5) for j in range(5)}

    # HTML table structure for the board
    board_html = """
    <table style="border-collapse: collapse; width: 100%; text-align: center;">
    """

    # Loop through 5 rows and 5 columns to create the board
    for i in range(5):
        board_html += "<tr>"
        for j in range(5):
            task = tasks[i * 5 + j]
            # Create a text input for each task
            response_key = f"q{i}{j}"
            current_response = st.session_state.responses[response_key]
            
            # Render the task with a text input inside each cell
            board_html += f'<td style="border: 1px solid black; padding: 20px; font-size: 18px; height: 120px; width: 120px;">'
            board_html += f'<div>{task}</div>'
            board_html += f'<div><input type="text" id="{response_key}" value="{current_response}" onchange="this.value=st.session_state.responses[\'{response_key}\']"></div>'
            board_html += '</td>'
        board_html += "</tr>"
    
    board_html += "</table>"

    # Display the bingo board using Markdown to render the HTML
    st.markdown(board_html, unsafe_allow_html=True)

# Function to display the board
st.title("🐾 Dog Care Bingo Board")
st.write("Complete the bingo board by answering questions about your dog's care. "
         "Enter your responses in the boxes below.")

# Call the function to display the board
create_bingo_board()

# Show a summary of the responses
st.subheader("Your Responses")
for key, value in st.session_state.responses.items():
    st.write(f"{key}: {value}")