FROM python:3.9
LABEL org.opencontainers.image.source https://github.com/adyavanapalli/say-great-again-bot

COPY . /say-great-again-bot
WORKDIR /say-great-again-bot

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
