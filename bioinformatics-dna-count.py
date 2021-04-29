import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

st.set_page_config(layout="centered")
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
This app counts the Nucleotide composition of the query DNA\n
        	""")
    with col3:
        st.image(image)
st.write('-by Mayur Machhi')

## Input Box

st.header('Enter DNA Sequence')

sequence_input = '>DNA Query 1\n GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT'

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
	""")

st.header('Input DNA Query')


placeholder = st.empty()
placeholder.text(sequence)

st.header('Output DNA Nucleotide Count')

## 1. Print dictionary
# st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)


### 1. Print text
st.subheader('1. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
# st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
# st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)




st.write("-App by Mayur Machhi")