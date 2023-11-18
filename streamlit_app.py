import streamlit as st
import subprocess
import time

# Function to run a command and append output to the session state
def run_command(cmd):
    if 'output' not in st.session_state or not cmd:
        st.session_state.output = ""

    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    # Read the output line by line and update session state
    for line in iter(process.stdout.readline, ''):
        st.session_state.output += line
        time.sleep(0.1)  # Small delay to allow for UI updates

# Streamlit UI
st.title("Run Shell Commands")

# Input for command
user_input = st.text_input("Enter a shell command")

# Button to run the command
if st.button('Run Command'):
    run_command(user_input)

# Display the output
st.text_area("Output", st.session_state.output, height=300)

# Rerun the app every few seconds to update the output
st_autorefresh_interval = 1  # seconds
st.experimental_rerun() if time.time() % st_autorefresh_interval < 0.1 else None
