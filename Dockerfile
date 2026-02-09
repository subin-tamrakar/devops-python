FROM python:3.10-alpine AS builder
LABEL maintainer work.subin.tamrakar@gmail.com
WORKDIR /pyapp
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--root-path", "/pyapp", "--host", "0.0.0.0", "--port", "8000", "--reload"]
