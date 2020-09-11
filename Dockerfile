FROM python:3-alpine
COPY GuessGame.py /
COPY Live.py /
COPY MainGame.py /
COPY MainScores.py /
COPY MemoryGame.py /
COPY Score.py /
COPY Scores.txt /
COPY Utils.py /
COPY e2e.py /
COPY chromedriver.exe /
RUN pip install selenium
RUN pip install flask
RUN chmod -R 777 ./
CMD [ "python3", "./MainScores.py" ]
