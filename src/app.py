import streamlit as st

st.title("サンプルアプリ")

## タイトル
st.write("こんにちは!!私の名前は{YOUR_NAME}です。")

## 文字入力
text = st.text_input("sample")
if text:
    st.write(f"入力された文字 : {text}")

st.write("-"*40)  # ハイフンを40個出す。

## テキストボックス(ボタン押下で反映)
text2 = st.text_input("sample2")
if st.button("出力"):
    st.balloons()
    st.write(f"入力された文字 : {text2}")

st.write("-"*40)  # ハイフンを40個出す。

## 画像の表示
st.image("src/images/pose_pien_uruuru_woman.png", width=500, caption="🥺")

st.write("-"*40)  # ハイフンを40個出す。

## 画像ファイルのアップロード。
image_file = st.file_uploader("画像ファイルをアップロードしてください。", type=['png', 'jpg'])
if image_file is not None:
    image_file_byte = image_file.read()
    st.image(image_file_byte, width=500)






