FROM python:3-alpine
WORKDIR src
COPY MainScores.py /src
COPY Scores.txt /src
COPY Utils.py /src
COPY e2e.py /src
COPY chromedriver.exe /src
RUN pip install selenium
RUN pip install flask
RUN chmod -R 777 ./
EXPOSE 8777
CMD [ "python", "MainScores.py" ]