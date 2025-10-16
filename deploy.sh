#!/bin/bash

# Скрипт деплоя на VPS/хостинг

echo "🚀 Начинаем деплой Semey-KM Factory System..."

# Обновляем систему
echo "📦 Обновляем систему..."
sudo apt update && sudo apt upgrade -y

# Устанавливаем Python и зависимости
echo "🐍 Устанавливаем Python и зависимости..."
sudo apt install -y python3 python3-pip python3-venv nginx supervisor

# Клонируем репозиторий (если еще не клонирован)
if [ ! -d "/var/www/semey-km" ]; then
    echo "📥 Клонируем репозиторий..."
    sudo git clone https://github.com/Anubizze/semey-km.git /var/www/semey-km
fi

# Переходим в директорию проекта
cd /var/www/semey-km

# Создаем виртуальное окружение
echo "🔧 Создаем виртуальное окружение..."
python3 -m venv venv
source venv/bin/activate

# Устанавливаем зависимости
echo "📚 Устанавливаем зависимости..."
pip install -r requirements.txt

# Инициализируем базу данных
echo "🗄️ Инициализируем базу данных..."
python init_all_data.py
python create_admin.py

# Создаем конфигурацию для Gunicorn
echo "⚙️ Создаем конфигурацию Gunicorn..."
sudo tee /etc/supervisor/conf.d/semey-km.conf > /dev/null <<EOF
[program:semey-km]
command=/var/www/semey-km/venv/bin/gunicorn --bind 0.0.0.0:5000 app:app
directory=/var/www/semey-km
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/semey-km.log
EOF

# Создаем конфигурацию Nginx
echo "🌐 Создаем конфигурацию Nginx..."
sudo tee /etc/nginx/sites-available/semey-km > /dev/null <<EOF
server {
    listen 80;
    server_name your-domain.com;  # Замените на ваш домен

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Активируем сайт
sudo ln -sf /etc/nginx/sites-available/semey-km /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Перезапускаем сервисы
echo "🔄 Перезапускаем сервисы..."
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start semey-km
sudo systemctl reload nginx

echo "✅ Деплой завершен!"
echo "🌐 Ваше приложение доступно по адресу: http://your-domain.com"
echo "📊 Логи приложения: sudo tail -f /var/log/semey-km.log"
