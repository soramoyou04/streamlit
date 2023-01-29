import streamlit as st

st.title('Streamlit 超入門')
st.write('MOCHI')

button=st.button('もちの写真')

st.image('https://github.com/soramoyou04/streamlit/blob/master/moti.jpg?raw=true',caption='もち',use_column_width=True)

if button:
    col1, col2, col3 = st.columns(3)
    ex=st.expander('ex')
    ex.write("A")
    ex.image('https://github.com/soramoyou04/streamlit/blob/master/moti.jpg?raw=true', use_column_width=True)

    with col1:
      st.header("A")
      st.image('https://github.com/soramoyou04/streamlit/blob/master/moti.jpg?raw=true', use_column_width=True)
