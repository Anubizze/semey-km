from werkzeug.security import generate_password_hash
from models import db, User
from app import app

with app.app_context():
    # Проверим, есть ли админ
    existing_admin = User.query.filter_by(username="admin").first()
    if not existing_admin:
        hashed_password = generate_password_hash("admin123")
        admin = User(
            fio="Администратор",
            iin="000000000000",
            username="admin",
            password=hashed_password,
            role="admin",
            position="Системный администратор"
        )
        db.session.add(admin)
        db.session.commit()
        print("✅ Админ создан! Логин: admin, Пароль: admin123")
    else:
        print("⚠️ Админ уже существует")
