import streamlit as st
import subprocess

# Function to run a command and stream the output
def run_command(cmd):
    if cmd:
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )

        # Collect and return the output
        output = ""
        for line in iter(process.stdout.readline, ''):
            output += line

        process.wait()
        return output, process.returncode

# Streamlit UI
st.title("Run Shell Commands")

# Input for command
user_input = st.text_input("Enter a shell command")

# Button to run the command
if st.button('Run Command'):
    output, returncode = run_command(user_input)
    st.text_area("Output", output, height=300)
    st.write(f"Command exited with return code {returncode}")
