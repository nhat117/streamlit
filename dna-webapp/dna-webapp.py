from lib2to3.pgen2.grammar import opmap
from re import X
from tkinter import E
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
        # DNA Nucleotide Count Web App
        This app counts the nucleotide composition of query DNA!
        
        ***
         """)

# Input text box
st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"


sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence 
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write(""" 
         ***
         """)

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## Prints the input DNA sequence
st.subheader('1.Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

x = DNA_nucleotide_count(sequence)

x 
### 2. Print text
st.subheader('2.Print text')
st.write('There are ' + str(x['A']) + ' adenine (A)')
st.write('There are ' + str(x['T']) + ' thymine (T)')
st.write('There are ' + str(x['G']) + ' guanine (G)')
st.write('There are ' + str(x['C']) + ' cytosine (C)')

## 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart using Altair')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)
p = p.properties(
    width = alt.Step(80) # controls width of bar.
)

st.write(p)

## End of the program