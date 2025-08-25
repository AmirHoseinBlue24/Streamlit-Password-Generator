import string
import random
import streamlit as st

def password_genrator(len:int = 8, symbol = False, digit = False):
    if symbol == False and digit == False:
        char = string.ascii_letters
    elif symbol == True and digit == False:
        char = string.ascii_letters + string.punctuation
    elif symbol == True and digit == True:
        char = string.ascii_letters + string.punctuation + string.digits
    else:
        char = string.ascii_letters + string.digits
    
    return ''.join(random.choice(char) for _ in range(len))

st.title("Password Generator")
length = st.slider("Length Password:", 8, 20)

symbols = st.checkbox("Has symbols?")
digits = st.checkbox("Has digits?")

st.write(password_genrator(length, symbols, digits))