#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app, db, Product, Equipment, Material, User
from werkzeug.security import generate_password_hash
from datetime import datetime

def init_all_data():
    with app.app_context():
        print("🚀 Инициализация всех данных...")
        print("=" * 50)
        
        # Создаем таблицы
        db.create_all()
        print("✅ Таблицы созданы")
        
        # Проверяем и создаем продукты
        if Product.query.count() == 0:
            products_data = [
                {"name": "Блок газобетонный D400", "product_code": "GB-D400-200", "description": "Газобетонный блок плотностью D400, размер 200мм"},
                {"name": "Блок газобетонный D500", "product_code": "GB-D500-200", "description": "Газобетонный блок плотностью D500, размер 200мм"},
                {"name": "Блок газобетонный D600", "product_code": "GB-D600-200", "description": "Газобетонный блок плотностью D600, размер 200мм"},
                {"name": "Блок газобетонный D400-300", "product_code": "GB-D400-300", "description": "Газобетонный блок плотностью D400, размер 300мм"},
                {"name": "Блок газобетонный D500-300", "product_code": "GB-D500-300", "description": "Газобетонный блок плотностью D500, размер 300мм"},
                {"name": "Перемычка газобетонная", "product_code": "GB-LINTEL", "description": "Перемычка из газобетона"},
                {"name": "U-блок газобетонный", "product_code": "GB-U-BLOCK", "description": "U-образный блок для армопоясов"}
            ]
            
            for prod_data in products_data:
                product = Product(**prod_data)
                db.session.add(product)
            
            print(f"✅ Создано {len(products_data)} продуктов")
        else:
            print(f"✅ Продукты уже существуют: {Product.query.count()}")
        
        # Проверяем и создаем оборудование
        if Equipment.query.count() == 0:
            equipment_data = [
                {"name": "Форма заливки №1", "equipment_type": "casting", "status": "operational"},
                {"name": "Форма заливки №2", "equipment_type": "casting", "status": "operational"},
                {"name": "Форма заливки №3", "equipment_type": "casting", "status": "operational"},
                {"name": "Станок резки №1", "equipment_type": "cutting", "status": "operational"},
                {"name": "Станок резки №2", "equipment_type": "cutting", "status": "operational"},
                {"name": "Автоклав №1", "equipment_type": "autoclave", "status": "operational"},
                {"name": "Автоклав №2", "equipment_type": "autoclave", "status": "operational"},
                {"name": "Автоклав №3", "equipment_type": "autoclave", "status": "operational"}
            ]
            
            for eq_data in equipment_data:
                equipment = Equipment(**eq_data)
                db.session.add(equipment)
            
            print(f"✅ Создано {len(equipment_data)} единиц оборудования")
        else:
            print(f"✅ Оборудование уже существует: {Equipment.query.count()}")
        
        # Проверяем и создаем материалы
        if Material.query.count() == 0:
            materials_data = [
                {"name": "Цемент", "unit": "kg"},
                {"name": "Известь", "unit": "kg"},
                {"name": "Алюминиевая пудра", "unit": "kg"},
                {"name": "Шлам", "unit": "l"},
                {"name": "Гипс", "unit": "kg"},
                {"name": "Вода", "unit": "l"},
                {"name": "Сульфанол", "unit": "l"},
                {"name": "Песок", "unit": "kg"},
                {"name": "Зола", "unit": "kg"}
            ]
            
            for mat_data in materials_data:
                material = Material(**mat_data)
                db.session.add(material)
            
            print(f"✅ Создано {len(materials_data)} материалов")
        else:
            print(f"✅ Материалы уже существуют: {Material.query.count()}")
        
        # Проверяем и создаем пользователей
        if User.query.count() == 0:
            users_data = [
                {"fio": "Администратор", "iin": "000000000000", "username": "admin", "password": "admin", "role": "admin", "position": "Системный администратор"},
                {"fio": "Директор Иванов И.И.", "iin": "111111111111", "username": "director", "password": "director123", "role": "director", "position": "Директор"},
                {"fio": "Главный технолог Петров П.П.", "iin": "222222222222", "username": "chief_tech", "password": "tech123", "role": "chief_technologist", "position": "Главный технолог"},
                {"fio": "Оператор резки Сидоров С.С.", "iin": "333333333333", "username": "cutting_op", "password": "cutting123", "role": "cutting_operator", "position": "Оператор резки"},
                {"fio": "Оператор автоклава Козлов К.К.", "iin": "444444444444", "username": "autoclave_op", "password": "autoclave123", "role": "autoclave_operator", "position": "Оператор автоклава"},
                {"fio": "Заливщик Морозов М.М.", "iin": "555555555555", "username": "casting_op", "password": "casting123", "role": "casting_operator", "position": "Заливщик"},
                {"fio": "Сотрудник Новиков Н.Н.", "iin": "666666666666", "username": "employee", "password": "employee123", "role": "employee", "position": "Сотрудник"}
            ]
            
            for user_data in users_data:
                # Хешируем пароль
                user_data["password"] = generate_password_hash(user_data["password"])
                user = User(**user_data)
                db.session.add(user)
            
            print(f"✅ Создано {len(users_data)} пользователей")
        else:
            print(f"✅ Пользователи уже существуют: {User.query.count()}")
        
        # Сохраняем все изменения
        db.session.commit()
        
        print("\n🎉 Инициализация завершена!")
        print("=" * 50)
        print("📋 Сводка:")
        print(f"  📦 Продукты: {Product.query.count()}")
        print(f"  🔧 Оборудование: {Equipment.query.count()}")
        print(f"  🧱 Материалы: {Material.query.count()}")
        print(f"  👥 Пользователи: {User.query.count()}")
        
        print("\n🔑 Данные для входа:")
        print("  admin / admin")
        print("  director / director123")
        print("  chief_tech / tech123")
        print("  cutting_op / cutting123")
        print("  autoclave_op / autoclave123")
        print("  casting_op / casting123")
        print("  employee / employee123")

if __name__ == "__main__":
    init_all_data()
