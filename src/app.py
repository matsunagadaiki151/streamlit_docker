import streamlit as st
from PIL import Image

st.title("Streamlit入門")

image_file = st.file_uploader("ファイルを選択してください。", type=["png", "jpg"])

if image_file is not None:
    image_byte_data = image_file.read()
    st.image(image_byte_data, width=500)  # byte型のデータも画像として表示できる。


