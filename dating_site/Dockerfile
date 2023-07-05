FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y
RUN pip install --upgrade pip
EXPOSE 8000
WORKDIR app/dating_site/
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /app/

CMD ["sh", "./bin/start_gunicorn.sh"]