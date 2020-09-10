FROM python:3
ADD WorldOfGames ./
RUN pip install random
RUN pip install selenium
RUN pip install flask
CMD [ "python", "./MainGame.py" ]
