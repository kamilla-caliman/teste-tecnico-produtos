FROM python:3.11.0-alpine

# Não utilizar os arquivos .pyc na construção da imagem
ENV PYTHONDONTWRITEBYTECODE 1

# Os logs de erro não se percam no buffer de texto do terminal
ENV PYTHONUNBUFFERED 1

WORKDIR /test_obrazul

COPY . /test_obrazul/

RUN pip install -U pip
RUN pip install -r requirements.txt
