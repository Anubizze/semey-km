from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(120), nullable=False)
    iin = db.Column(db.String(12), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(30), nullable=False)  # Расширили для новых ролей
    position = db.Column(db.String(100), nullable=False)

    # связи
    entries = db.relationship("Entry", backref="user")
    batches = db.relationship("Batch", backref="user")

class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=True)
    batch_number = db.Column(db.String(50), unique=True, nullable=False)
    batch_type = db.Column(db.String(20), nullable=False)  # casting, cutting, autoclave
    status = db.Column(db.String(20), nullable=False, default="active")  # active, completed, cancelled, inactive
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    end_time = db.Column(db.DateTime, nullable=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id"), nullable=True)
    shift = db.Column(db.String(20), nullable=False, default="day")  # day, night
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)
    
    # связи
    materials = db.relationship("BatchMaterial", backref="batch")

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(50), nullable=False)  # mixer, cutter, autoclave
    status = db.Column(db.String(20), nullable=False, default="operational")  # operational, maintenance, broken
    
    # связи
    batches = db.relationship("Batch", backref="equipment")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product_code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    # связи
    batches = db.relationship("Batch", backref="product")

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(20), nullable=False)  # kg, l, pieces
    is_active = db.Column(db.Boolean, default=True)

class BatchMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer, db.ForeignKey("batch.id"), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey("material.id"), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    recorded_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    # связи
    material = db.relationship("Material", backref="batch_materials")

class BatchTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    batch_type = db.Column(db.String(20), nullable=False)  # casting, cutting, autoclave
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id"), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    
    # связи
    product = db.relationship("Product", backref="templates")
    equipment = db.relationship("Equipment", backref="templates")
    creator = db.relationship("User", backref="created_templates")
    materials = db.relationship("BatchTemplateMaterial", backref="template")

class BatchTemplateMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey("batch_template.id"), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey("material.id"), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    
    # связи
    material = db.relationship("Material", backref="template_materials")

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    # Материалы
    cement = db.Column(db.Float, default=0)
    lime = db.Column(db.Float, default=0)
    alum_powder = db.Column(db.Float, default=0)
    sludge = db.Column(db.Float, default=0)
    gypsum = db.Column(db.Float, default=0)
    water = db.Column(db.Float, default=0)
    sulfanol = db.Column(db.Float, default=0)

    # Время и смена
    time = db.Column(db.String(10), nullable=False)
    shift = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)
