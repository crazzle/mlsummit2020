FROM python:3.7

ADD configs/tini /tini
RUN chmod +x /tini

ADD configs/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
WORKDIR /mlessentials

ADD requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8888
ENTRYPOINT ["/tini", "--", "jupyter", "lab"]
