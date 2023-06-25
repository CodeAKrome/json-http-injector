FROM python:3.10-slim-buster
WORKDIR /app
COPY src-requirements.txt .
RUN pip install --no-cache-dir -r src-requirements.txt
COPY src .
CMD ["uvicorn", "micro-gp:app", "--host", "0.0.0.0", "--port", "31337"]
