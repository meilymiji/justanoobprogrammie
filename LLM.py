import streamlit as st
import nltk
import pandas as pd
import spacy #part of speech
from googletrans import Translator

prompt = """Act as a teacher in elementary, secondary and high school teacher. 
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

#เอา user_input ไปตัดเป็นคำๆ แล้วเอาคำมาแมทช์กับลิสต์คำศัพท์ระดับประภม มัธยมต้นปลาย แล้วสร้่างใส่ในดิกที่มีvalueเป็นtuple ประกอบด้วย ชนิดของคำ คำแปล ตัวอย่างประโยคการใช้ (หา library ลิสต์คำศัพท์ คำแปลไทย ตัวอย่างประโยค

if st.button("Submit"):
    return output
