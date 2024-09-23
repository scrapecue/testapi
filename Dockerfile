FROM python:3.7-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENV PYTHONUNBUFFERED=1
ENTRYPOINT [ "sh", "start_server.sh" ]
EXPOSE 8455