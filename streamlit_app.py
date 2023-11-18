import streamlit as st
import time
import os

# Function to start the command in the background
def start_command(cmd):
    output_file = "command_output.txt"
    os.system(f"{cmd} > {output_file} 2>&1 &")
    return output_file

# Function to read the output file and update session state
def update_output(output_file):
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            st.session_state.output = file.read()

# Streamlit UI
st.title("Run Shell Commands")

# Input for command
user_input = st.text_input("Enter a shell command")

# Button to run the command
if st.button('Run Command'):
    # Clear previous output
    st.session_state.output = ""
    output_file = start_command(user_input)
    st.session_state.output_file = output_file

# Display the output
if 'output' not in st.session_state:
    st.session_state.output = ""

st.text_area("Output", st.session_state.output, height=300)

# Periodically update the output
if 'output_file' in st.session_state:
    update_output(st.session_state.output_file)
    time.sleep(1)
    st.experimental_rerun()
