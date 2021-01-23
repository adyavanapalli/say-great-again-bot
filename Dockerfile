FROM python:3.9

COPY . /say-great-again-bot
WORKDIR /say-great-again-bot

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
