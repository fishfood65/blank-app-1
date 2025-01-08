import streamlit as st

# Title of the app
st.title("Name Input Form")

# Initialize session state to track if the name has been submitted
if 'name_submitted' not in st.session_state:
    st.session_state.name_submitted = False
    st.session_state.name = ""

# Show form to enter name if it hasn't been submitted
if not st.session_state.name_submitted:
    # Create a form to ask for the user's name
    with st.form(key="name_form"):
        # Display the input field for the name
        name = st.text_input("What is your name?")
        
        # Submit button
        submit_button = st.form_submit_button("Submit")
    
    # When the form is submitted, save the name and mark it as submitted
    if submit_button and name:
        st.session_state.name = name
        st.session_state.name_submitted = True
        st.write(f"Hello, {name}! Your name has been successfully recorded.")
else:
    # If the name is already submitted, display the name and disable further changes
    st.write(f"Hello, {st.session_state.name}! Your name has been submitted and cannot be changed.")