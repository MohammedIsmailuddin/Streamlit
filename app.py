import streamlit as st

# Title of the Streamlit app
st.title("Simple Streamlit Text App")

# User input section
user_input = st.text_input("Enter some text:")

# If the user has entered some text, display it back along with the text length
if user_input:
    st.write(f"You entered: {user_input}")
    st.write(f"Length of the text: {len(user_input)} characters")

# Adding some additional functionalities for demonstration
st.subheader("Text Transformation")

# Convert text to uppercase
if st.button("Convert to Uppercase"):
    st.write(user_input.upper())

# Convert text to lowercase
if st.button("Convert to Lowercase"):
    st.write(user_input.lower())

# Display the reversed text
if st.button("Reverse Text"):
    st.write(user_input[::-1])