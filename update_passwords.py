#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app, db, User
from werkzeug.security import generate_password_hash

def update_passwords():
    with app.app_context():
        # Обновляем пароли для всех пользователей
        users = User.query.all()
        
        # Стандартные пароли для тестирования
        passwords = {
            'admin': 'admin123',
            'director': 'director123', 
            'chief_technologist': 'tech123',
            'cutting_operator': 'cutting123',
            'autoclave_operator': 'autoclave123',
            'casting_operator': 'casting123',
            'employee': 'employee123'
        }
        
        for user in users:
            if user.username in passwords:
                new_password = passwords[user.username]
                user.password = generate_password_hash(new_password)
                print(f"Обновлен пароль для {user.username}: {new_password}")
            else:
                # Для остальных пользователей устанавливаем пароль по умолчанию
                user.password = generate_password_hash('password123')
                print(f"Установлен пароль по умолчанию для {user.username}: password123")
        
        db.session.commit()
        print("\n✅ Все пароли обновлены!")
        print("\n📋 Список пользователей и паролей:")
        print("=" * 50)
        for user in users:
            if user.username in passwords:
                print(f"👤 {user.username:20} | 🔑 {passwords[user.username]:15} | 👔 {user.role}")
            else:
                print(f"👤 {user.username:20} | 🔑 password123      | 👔 {user.role}")

if __name__ == "__main__":
    update_passwords()


