FROM python:3.11-slim

LABEL maintainer="Harishmaran Subbaiah Thirumaran <harishmaran2001@gmail.com>"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .

ENV ENVIRONMENT=production
EXPOSE 8081

HEALTHCHECK --interval=15s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8081/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
