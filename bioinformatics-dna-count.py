import pandas as pd
import streamlit as st
import altair as alt

## Title

st.write("""

# DNA Nucleotide Counter

This app counts the Nucleotide composition of the query DNA
	""")

## Input Box

st.header('Enter DNA Sequence')