FROM python:3-alpine
WORKDIR src
COPY MainScores.py /src
COPY Scores.txt /src
COPY Utils.py /src
COPY requirements.txt /src
RUN python3 -m pip install -r requirements.txt
RUN chmod -R 777 ./
EXPOSE 8777
CMD [ "python3", "MainScores.py" ]
