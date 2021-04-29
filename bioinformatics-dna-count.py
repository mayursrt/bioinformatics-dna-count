import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

## Title

title_container = st.beta_container()
col1, col2, col3 = st.beta_columns([1, 7, 1])
image = Image.open('assets/logo.jpg')
with title_container:
    with col1:
        st.image(image)
    with col2:
        st.write("""
        	# DNA Nucleotide Counter App\n
        	This app counts the Nucleotide composition of the query DNA

        	""")
    with col3:
        st.image(image)


## Input Box

st.header('Enter DNA Sequence')

sequence_input = '>DNA Query 1\n GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT'

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string