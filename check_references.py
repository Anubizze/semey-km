#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app, db, Product, Equipment, Material, User

def check_references():
    with app.app_context():
        print("🔍 Проверка справочников...")
        print("=" * 50)
        
        # Проверяем продукты
        products = Product.query.filter_by(is_active=True).all()
        print(f"📦 Активные продукты: {len(products)}")
        for product in products:
            print(f"  - {product.product_code}: {product.name}")
        
        # Проверяем оборудование
        equipment = Equipment.query.filter_by(status="operational").all()
        print(f"\n🔧 Рабочее оборудование: {len(equipment)}")
        for eq in equipment:
            print(f"  - {eq.name} ({eq.equipment_type})")
        
        # Проверяем материалы
        materials = Material.query.filter_by(is_active=True).all()
        print(f"\n🧱 Активные материалы: {len(materials)}")
        for material in materials:
            print(f"  - {material.name} ({material.unit})")
        
        # Проверяем пользователей
        users = User.query.all()
        print(f"\n👥 Пользователи: {len(users)}")
        for user in users:
            print(f"  - {user.username} ({user.role})")
        
        print("\n" + "=" * 50)
        
        # Проверяем доступность для форм
        print("📋 Проверка доступности для форм:")
        
        # Форма создания партий
        print(f"  ✅ create_batch: {len(products)} продуктов, {len(equipment)} оборудования")
        
        # Форма резчика
        cutters = Equipment.query.filter_by(equipment_type="cutting", status="operational").all()
        print(f"  ✅ cutting_dashboard: {len(cutters)} резчиков")
        
        # Форма автоклавщика
        autoclaves = Equipment.query.filter_by(equipment_type="autoclave", status="operational").all()
        print(f"  ✅ autoclave_dashboard: {len(autoclaves)} автоклавов")
        
        # Форма добавления материалов
        print(f"  ✅ add_material_to_batch: {len(materials)} материалов")
        
        print("\n🎉 Проверка завершена!")

if __name__ == "__main__":
    check_references()


