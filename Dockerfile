FROM python:3.8

COPY . /opt/app

WORKDIR /opt/app

RUN pip install streamlit

EXPOSE 8501

# 一度bashに入りたい場合はこちらを実行
# CMD ["bash"]

ENTRYPOINT [ "streamlit", "run"]

CMD [ "src/app.py" ]