import streamlit as st
import subprocess
import threading

# Function to run a command and stream the output
def run_command(cmd):
    st.write(f"Running: `{cmd}`\n")
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    # Stream the output
    for line in iter(process.stdout.readline, ''):
        st.write(line)
    
    process.wait()
    st.write(f"---\nCommand exited with return code {process.returncode}")

# Function to run the command in a separate thread
def run_command_threaded(cmd):
    if cmd:
        thread = threading.Thread(target=run_command, args=(cmd,))
        thread.start()

# Streamlit UI
st.title("Run Shell Commands")

# Input for command
user_input = st.text_input("Enter a shell command")

# Button to run the command
if st.button('Run Command'):
    run_command_threaded(user_input)
