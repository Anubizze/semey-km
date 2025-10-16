#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app, db, Product, Equipment, Material

def check_data():
    with app.app_context():
        print("🔍 Проверяем данные в базе...")
        print("=" * 50)
        
        # Проверяем продукты
        products = Product.query.all()
        print(f"📦 Продукты: {len(products)}")
        for product in products:
            print(f"  - {product.product_code}: {product.name}")
        
        # Проверяем оборудование
        equipment = Equipment.query.all()
        print(f"\n🔧 Оборудование: {len(equipment)}")
        for eq in equipment:
            print(f"  - {eq.name}")
        
        # Проверяем материалы
        materials = Material.query.all()
        print(f"\n🧱 Материалы: {len(materials)}")
        for material in materials:
            print(f"  - {material.name} ({material.unit})")
        
        if len(products) == 0:
            print("\n❌ Продукты отсутствуют! Нужно создать.")
            return False
        else:
            print(f"\n✅ Найдено {len(products)} продуктов")
            return True

if __name__ == "__main__":
    check_data()


