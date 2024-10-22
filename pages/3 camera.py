import streamlit as st

st.title('Camera')

image = st.camera_input('Take a selfie')

if image:
    st.image(image, caption='Your photo', use_column_width=True)
