import streamlit as st
import os

st.title('Photo Gallery')

# read file names from photos folder

photos = os.listdir('photos')

for i in range(0, len(photos), 2):
    cols = st.columns(2)  # Create two columns

    # Display the images in each column
    if i < len(photos):
        image = open(f'photos/{photos[i]}', 'rb').read()
        cols[0].image(image, caption=photos[i], use_column_width=True)

    if i + 1 < len(photos):
        image = open(f'photos/{photos[i+1]}', 'rb').read()
        cols[1].image(image, caption=photos[i + 1], width=300)