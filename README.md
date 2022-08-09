# Streamlit Study

## 1. 開発環境

Docker を用いた仮想環境にコンテナを立ちあげます。

## 2. Docker イメージの作成

1. `Dockerfile`があるディレクトリで docker イメージをビルドします。<br>
   `docker image build -t streamlit_study_img .`

※ いきなり streamlit を起動したい場合は`Dockerfile`を修正してください。

## 3. 開発環境立ち上げ手順

ビルドが終わったら作ったイメージを元にコンテナを立ち上げます。<br>

### 3-1. コンテナ内で編集する場合

1. 以下で、コンテナを立ち上げ、環境内に入ります。<br>
   `docker container run --name streamlit_study_container -it -p 8501:8501 streamlit_study_img`

2. Streamlit ファイルを実行するには`/opt/app/src`直下で`streamlit run app.py`と実行します。

3. コンテナ環境内で vim をインストールするか、VSCode 等のエディタの Docker 拡張機能を利用することによって Python ファイルを編集し、アプリをホットリロードすることができます。<br>
   (※コンテナを切断すると編集内容はリセットされます。)

### 3-2. いきなり Streamlit を立ち上げる場合

1. 以下で、コンテナを立ち上げます。<br>
   `docker container run --name streamlit_study_container --mount type=bind,source="$(pwd)"/src,target=/opt/app/src -p 8501:8501 streamlit_study_img`

2. `localhost:8501` にアクセスすると開発中のサイトにアクセスできます。

## 4. 開発環境の終了手順

1. docker を動かしているターミナルで`ctrl-c`、または別のターミナルで`docker container stop streamlit_study_container`で実行中の docker のプロセスを停止する

## 5. コンテナ、イメージの破棄（全ての開発が終わった）

1. `docker rm streamlit_study_container`でコンテナを削除する

2. `docker rmi streamlit_study_img`でイメージを削除する
