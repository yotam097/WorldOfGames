FROM python:3-alpine
COPY WorldOfGames /
RUN pip install random
RUN pip install selenium
RUN pip install flask
CMD [ "python3", "./MainGame.py" ]
