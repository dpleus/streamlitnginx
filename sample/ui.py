import streamlit as st
import os
import time

st.title("Hello Captain")

file_to_be_uploaded = st.file_uploader("Choose a file", type=['MP3', 'WAV'])

RAWDATAPATH = ""


def save_uploadedfile(uploadedfile):
    global RAWDATAPATH
    with open(os.path.join(RAWDATAPATH, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())

        with st.spinner(text="Uploading . . ."):
            time.sleep(3)

    bala = os.path.join(RAWDATAPATH, uploadedfile.name)

    print(bala)

    return bala


if st.button("Upload"):
    if file_to_be_uploaded is not None:
        input_files = save_uploadedfile(file_to_be_uploaded)
        st.write(f"File is uploaded in {input_files} path")

        # Audio Files Listening
        audio_file = open(input_files, 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/wav', start_time=0)