# Streamlit Study

## 1. 開発環境

Docker を用いた仮想環境にコンテナを立ちあげます。

## 2. Docker イメージの作成

1. `DockerFile`があるディレクトリで docker イメージをビルドします。<br>
   `docker image build -t streamlit_study_img .`

## 3. 開発環境立ち上げ手順

1. ビルドが終わったら作ったイメージを元にコンテナを立ち上げます。<br>
   `docker container run --name streamlit_study_container -p 8501:8501 streamlit_study_img`

2. `localhost:8501` にアクセスすると開発中のサイトにアクセスできます。

## 4. 開発環境の修了手順

1. docker を動かしているターミナルで`ctrl-c`、または別のターミナルで`docker container stop streamlit_study_container`で実行中の docker のプロセスを停止する

## 5. コンテナ、イメージの破棄（全ての開発が終わった）

1. `docker rm streamlit_study_container`でコンテナを削除する

2. `docker rmi streamlit_study_img`でイメージを削除する
