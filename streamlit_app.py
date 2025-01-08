import streamlit as st

# Initialize session state to track whether the input has been entered
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Display the clickable icon (using a button as an icon here)
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Display the clickable icon (emoji)
if not st.session_state.clicked:
    if st.button("🖼️ Click me"):
        # When clicked, show text input box and hide the icon
        st.session_state.clicked = True
else:
    # Show the text input box
    user_input = st.text_input("Enter your text:")

    # Once text is entered, hide the input box and show the check mark icon
    if user_input:
        st.session_state.user_input = user_input
        st.write(f"✔️ You entered: {st.session_state.user_input}")
        st.session_state.clicked = False  # Optionally reset to allow a new round