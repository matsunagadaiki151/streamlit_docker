FROM python:3.8

COPY . /opt/app

WORKDIR /opt/app/src

# VSCodeのDocker拡張を使わない場合
# RUN apt-get update && apt-get install -y vim

RUN pip install streamlit

EXPOSE 8501

CMD ["bash"]

# いきなりstreamlitを起動する場合はbashをコメントアウトし、以下を実行。
# ENTRYPOINT [ "streamlit", "run"]

# CMD [ "app.py" ]