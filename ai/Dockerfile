# Dockerfile for the trading dashboard AI components
FROM python:3.9

WORKDIR /app
COPY requirements.txt .
COPY insight_generator.py .
COPY predictive_model.py .

RUN pip install -r requirements.txt

CMD ["python", "insight_generator.py"]