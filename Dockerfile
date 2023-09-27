# Install pkg-config and its libraries
RUN apt-get install -y pkg-config libmysqlclient-dev


# Установите директорию для Django
ENV DJANGO_SETTINGS_MODULE=mysite.settings

COPY mysite/ /app/mysite/
COPY run.sh /app/mysite/

# Скопируйте зависимости проекта и установите их
RUN pip install -r /app/mysite/requirements.txt

# Установка дополнительных зависимостей
RUN apt-get install -y libnss3 libgdk-pixbuf2.0-0 libgtk-3-0

# Создайте рабочую директорию
WORKDIR /app/mysite 

# Выполните парсинг данных
# CMD ["python3", "/app/mysite/scripts/parser.py"]

CMD ["sh", "/app/mysite/run.sh"]