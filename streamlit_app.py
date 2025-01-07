import streamlit as st

# Title of the app
st.title("One Question Form")

# Create a form to collect the answer to a single question
with st.form(key="question_form"):
    # Display the question and text input box for the answer
    answer = st.text_input("What is your favorite color?")
    
    # Submit button
    submit_button = st.form_submit_button("Submit ✔️")  # Icon on the button

# When the form is submitted, show the result
if submit_button:
    if answer:
        st.write(f"Thank you for your submission! Your favorite color is: {answer}")
    else:
        st.write("You didn't provide an answer. Please try again!")