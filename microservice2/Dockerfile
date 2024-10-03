FROM python:3.12

WORKDIR /myLasmina

COPY requirements.txt .
RUN pip install -r requirements2.txt

COPY . .

EXPOSE 5001

CMD ["python", "server.py"]