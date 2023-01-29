import streamlit as st
from PIL import Image

st.title('Streamlit 超入門')
st.write('MOCHI')
img=Image.open("moti.JPG")
st.image(img,caption='もち',use_column_width=True)
