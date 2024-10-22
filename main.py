import streamlit as st
import requests

st.title('Hello World')

st.write('This is a simple Streamlit app.')

st.header('Website Navigation')
st.divider()

st.page_link('pages/1 search.py', label='Search the web', icon='🔍')
st.page_link('pages/2 gallery.py', label='Image gallery', icon='🖼️')
st.page_link('pages/3 camera.py', label='Camera', icon='📸')
st.page_link('pages/4 about.py', label='About this app', icon='📄')