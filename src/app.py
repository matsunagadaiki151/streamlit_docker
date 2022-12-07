import streamlit as st
import io
import os

from google.cloud import vision

# タイトル
st.title("文字検出アプリ")

## 画像ファイルのアップロード。
image_file = st.file_uploader("画像ファイルをアップロードしてください。", type=['png', 'jpg'])
if image_file is not None:
    image_file_byte = image_file.read()
    image = vision.Image(content=image_file_byte)
    st.image(image_file_byte, width=500)

    # クライアントを定義
    client = vision.ImageAnnotatorClient()
    # ラベル抽出を適用
    response = client.text_detection(image=image)
    annotations = response.text_annotations

    st.write("検出された文字")
    for annotation in annotations:
        st.write(annotation.description)







