FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY __main__.py solax.py ./

RUN useradd --create-home --uid 1000 app
USER app

CMD ["python", "__main__.py"]
