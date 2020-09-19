FROM python:3-alpine
WORKDIR src
COPY MainScores.py /src
COPY Scores.txt /src
COPY Utils.py /src
RUN pip install flask
RUN pip install docker
RUN pip install pymysql
RUN chmod -R 777 ./
EXPOSE 8777
CMD [ "python", "MainScores.py" ]