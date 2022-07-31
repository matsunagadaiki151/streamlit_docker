FROM python:3.8

COPY . /opt/app

WORKDIR /opt/app/src

RUN pip install streamlit

EXPOSE 8501

CMD ["bash"]

# いきなりstreamlitを起動する場合はbashをコメントアウトし、以下を実行。
# ENTRYPOINT [ "streamlit", "run"]

# CMD [ "app.py" ]