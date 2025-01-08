import streamlit as st

# Initialize session state to track stages and data
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Callback to advance to the next stage
def advance_stage():
    if st.session_state.stage < 3:
        st.session_state.stage += 1

# Callback to reset the flow to stage 0
def reset_stage():
    st.session_state.stage = 0
    st.session_state.user_name = ""

# Stage 0: Before the user begins
if st.session_state.stage == 0:
    st.title("Welcome!")
    st.write("Click the button below to start.")
    if st.button("Start"):
        advance_stage()  # Advance to stage 1

# Stage 1: User enters their name
elif st.session_state.stage == 1:
    st.title("Enter your name")
    if 'name_submitted' not in st.session_state or not st.session_state.name_submitted:
        user_name = st.text_input("What is your name?", key="name_input")
        submit_button = st.button("Submit")
        
        # Once the user submits their name, store it and prevent further edits
        if submit_button and user_name:
            st.session_state.user_name = user_name
            st.session_state.name_submitted = True
            advance_stage()  # Move to stage 2
        elif submit_button and not user_name:
            st.warning("Please enter your name!")
    else:
        # If name is submitted, show the name and disable further input
        st.write(f"Your name is {st.session_state.user_name}. You cannot change it.")
        advance_stage()  # Automatically move to stage 2

# Stage 2: Thank you message
elif st.session_state.stage == 2:
    st.title(f"Thank you, {st.session_state.user_name}!")
    st.write("We appreciate your submission.")
    advance_stage()  # Automatically move to stage 3

# Stage 3: Reset button
elif st.session_state.stage == 3:
    st.title("Process Completed!")
    st.write(f"Thank you for participating, {st.session_state.user_name}!")
    if st.button("Reset Process"):
        reset_stage()  # Reset everything and go back to stage 0