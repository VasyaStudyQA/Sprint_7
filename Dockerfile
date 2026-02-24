FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости отдельно (для кэширования)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Команда запуска тестов
CMD ["pytest", "-v", "--alluredir=allure-results", "allure serve allure_results"]