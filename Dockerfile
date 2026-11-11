FROM python:3.14-slim
WORKDIR /app
COPY . .
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
