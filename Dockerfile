FROM python:3.8

COPY . /opt/app
WORKDIR /opt/app/src

RUN pip install streamlit

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run"]

CMD [ "app.py" ]