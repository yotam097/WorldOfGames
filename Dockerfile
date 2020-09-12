FROM python:3-alpine
WORKDIR src
COPY MainScores.py /src
COPY Score.py /src
COPY Scores.txt /src
RUN pip install flask
RUN chmod -R 777 ./
EXPOSE 8777
CMD [ "python3", "./MainScores.py" ]
