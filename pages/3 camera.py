import streamlit as st

st.set_page_config(page_title='Hello World', page_icon='👋', layout='wide')
st.title('Camera')

image = st.camera_input('Take a selfie')

if image:
    st.image(image, caption='Your photo', use_column_width=True)
