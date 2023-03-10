import streamlit as st
import os

img_path = os.path.join(os.path.dirname(__file__), 'images')
st.subheader('학생 사진 촬영')

col1, col2 = st.columns(2)

hakbun = col1.text_input('학번')
name = col2.text_input('성명')

pic = st.camera_input('사진찍기')

if pic is not None:
    img_name = hakbun+name
    frame, ext = os.path.splitext(pic.name)
    with open(os.path.join(img_path, img_name+ext), 'wb') as f:
        f.write(pic.getbuffer())

file_list = os.listdir(img_path)
st.write(file_list)

for fname in file_list:
    st.write(fname)
    with open(os.path.join(img_path, fname), 'rb') as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name=fname,
            mine='image/jpg'
        )

