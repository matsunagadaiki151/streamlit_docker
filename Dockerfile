FROM python:3.8

COPY . /opt/app

WORKDIR /opt/app

RUN pip install streamlit && \
    pip install --upgrade google-cloud-vision
RUN mkdir /tmp/keys/ && \
    touch /tmp/keys/key.json

# wakeupcat.jpgが閉鎖されていたため、いらすとやの素材で代用する。
RUN mkdir resources/ && wget https://4.bp.blogspot.com/-gX99oMun4bM/U9y_wYoE0EI/AAAAAAAAjiU/DHdcIfImCwQ/s800/pose_ganbarou_man.png -P /opt/app/resources/

ENV GOOGLE_APPLICATION_CREDENTIALS /tmp/keys/key.json

EXPOSE 8501

# 一度bashに入りたい場合はこちらを実行
# CMD ["bash"]

# いきなりstreamlitを立ち上げたいときはこちらを実行
ENTRYPOINT [ "streamlit", "run"]

CMD [ "src/app.py" ]