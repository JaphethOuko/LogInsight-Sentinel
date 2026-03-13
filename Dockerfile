FROM python:3.10-slim

# Install security updates to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN pip install requests
COPY monitor.py .
CMD ["python", "monitor.py"]