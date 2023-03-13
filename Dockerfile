FROM tiangolo/uvicorn-gunicorn-fastapi:latest

WORKDIR /backend

COPY ./backend /backend

RUN pip install -r requirements.txt
