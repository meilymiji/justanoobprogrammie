import streamlit as st
import nltk
import pandas as pd
import spacy #part of speech
import pythaidict #แปลเป็นไทย

prompt = """Act as a teacher in elmentary, secondary and high school. 
            You will recieve an english article. 
            List the words that appropiate from elementary, secondary and high school students. One word should have 3 things:
            -part of speech
            -that word meaning in Thai
            -example sentence
        """

st.title("English Teacher")
st.markdown("Input the article that you interasted in the box below. \n\
            I will hep you to learn English from what you're interested in by giving the words. :)")

user_input = st.text_area ("Enter you intersting article here")

def extract_word(user_input):
    pass
#if st.button("Submit"):
    #return output
