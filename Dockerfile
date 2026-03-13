FROM python:3.10-slim
RUN pip install requests
COPY monitor.py .
CMD ["python", "monitor.py"]