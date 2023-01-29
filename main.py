import streamlit as st
import os
from PIL import Image

path = os.path.dirname(__file__)
st.title('Streamlit 超入門')
st.write('MOCHI')
img=Image.open(path+'/moti.JPG')
st.image(img,caption='もち',use_column_width=True)
