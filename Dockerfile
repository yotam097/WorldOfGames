FROM python:3-alpine
WORKDIR src
COPY MainScores.py /src
COPY Score.py /src
COPY Scores.txt /src
RUN pip install flask

CMD [ "python", "./MainScores.py" ]
