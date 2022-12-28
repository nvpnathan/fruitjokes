FROM python:3.11-buster

MAINTAINER nvpnathan

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# for migrations
COPY migrations .
COPY pyproject.toml .

COPY app/ .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
