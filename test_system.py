#!/usr/bin/env python3
"""
Скрипт для тестирования расширенной системы управления заводом
"""

from werkzeug.security import generate_password_hash
from models import db, User, Batch, Equipment, Material
from app import app

def test_system():
    with app.app_context():
        print("🧪 Тестирование системы управления заводом...")
        
        # 1. Проверяем, что админ создан
        admin = User.query.filter_by(username="admin").first()
        if admin:
            print("✅ Администратор найден")
        else:
            print("❌ Администратор не найден")
            return
        
        # 2. Создаем тестовые роли
        test_users = [
            ("Иван Петров", "123456789012", "casting_operator", "Заливщик"),
            ("Мария Сидорова", "123456789013", "cutting_operator", "Резчик"),
            ("Алексей Козлов", "123456789014", "autoclave_operator", "Автоклавщик"),
            ("Елена Директорова", "123456789015", "chief_technologist", "Главный технолог")
        ]
        
        for fio, iin, role, position in test_users:
            existing = User.query.filter_by(iin=iin).first()
            if not existing:
                user = User(
                    fio=fio,
                    iin=iin,
                    username=iin,
                    password=generate_password_hash(iin[-6:]),
                    role=role,
                    position=position
                )
                db.session.add(user)
                print(f"✅ Создан пользователь: {fio} ({role})")
            else:
                print(f"⚠️ Пользователь уже существует: {fio}")
        
        db.session.commit()
        
        # 3. Проверяем материалы
        materials_count = Material.query.count()
        if materials_count > 0:
            print(f"✅ Материалы в справочнике: {materials_count}")
        else:
            print("⚠️ Справочник материалов пуст - запустите /init_references")
        
        # 4. Проверяем оборудование
        equipment_count = Equipment.query.count()
        if equipment_count > 0:
            print(f"✅ Оборудование в справочнике: {equipment_count}")
        else:
            print("⚠️ Справочник оборудования пуст - запустите /init_references")
        
        # 5. Проверяем партии
        batches_count = Batch.query.count()
        print(f"📦 Партий в системе: {batches_count}")
        
        print("\n🎯 Система готова к тестированию!")
        print("📋 Доступные учетные записи:")
        print("   Админ: admin / admin123")
        for fio, iin, role, position in test_users:
            print(f"   {position}: {iin} / {iin[-6:]}")
        
        print("\n🔗 Доступные функции:")
        print("   • Создание партий: /create_batch")
        print("   • Список партий: /batch_list")
        print("   • Инициализация справочников: /init_references")
        print("   • Аналитика: /director_dashboard")

if __name__ == "__main__":
    test_system()
