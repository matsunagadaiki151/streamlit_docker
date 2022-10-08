import streamlit as st
from PIL import Image  # 画像表示に必要

## タイトル
st.title("Streamlit入門")

## 文字入力
st.write("私の名前はYOUR_NAMEです。")

st.write("-"*40)  # ハイフンを40個出す。

# テキストボックス(入力後反映)
text = st.text_input("sample")
if text:
    st.write(f"テキストボックスの値 : {text}")

st.write("-"*40)  # ハイフンを40個出す。

# テキストボックス(ボタン押下で反映)
text2 = st.text_input("sample2", value="初期値")

if st.button("表示"):
    st.write(f"テキストボックスの値 : {text2}")

st.write("-"*40)  # ハイフンを40個出す。

# 画像の表示
st.write("画像の表示")
image = Image.open("src/images/pose_pien_uruuru_woman.png")
st.image(image, caption='🥺', width=500)

st.write("-"*40)  # ハイフンを40個出す。

# 画像ファイルのアップロード
image_file = st.file_uploader("ファイルを選択してください。", type=["png", "jpg"])

if image_file is not None:
    image_byte_data = image_file.read()
    st.image(image_byte_data, width=500)  # byte型のデータも画像として表示できる。






