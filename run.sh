!!#bin/bash

python3 /app/mysite/scripts/parser.py
python3 /app/mysite/scripts/manage.py runserver 0.0.0.0:8080

tail -f /dev/null