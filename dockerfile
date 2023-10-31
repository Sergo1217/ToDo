FROM python:3.12
RUN pip install poetry
COPY . /app
WORKDIR /app
RUN poetry update
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]