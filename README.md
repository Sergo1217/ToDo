# Unit of Work Pattern в FastAPI

Данный проект демонстрирует работу Unit of Work паттерна на примере FastAPI.

Запустить прект можно двумя способами.

## 1. Poetry

1. ```shell
   git clone https://github.com/Sergo1217/ToDo
   ```

2. ```shell
   cd ToDo
   ```

3. ```shell
   pip install poetry
   ```

4. ```shell
   poetry update
   ```

5. ```shell
   poetry run uvicorn main:app --host localhost --port 8000 --reload
   ```

## 2. Docker

1. ```shell
   git clone https://github.com/Sergo1217/ToDo
   ```

2. ```shell
   cd ToDo
   ```

3. ```shell
   docker build --pull --rm -f "dockerfile" -t todo:latest .
   ```

4. ```shell
   docker run -it --rm -p 8000:8000 -v .:/app todo  
   ```
