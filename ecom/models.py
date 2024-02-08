from tortoise.models import Model
from tortoise import fields

class Register(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(200)
    email = fields.CharField(200)
    password = fields.CharField(250)
    is_active = fields.BooleanField(default=True)
    last_login = fields.DatetimeField(auto_now=True)
    created = fields.DatetimeField(auto_now=True)
    

class Category(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(250)
    category_image = fields.TextField()
    description = fields.TextField()
    is_active = fields.BooleanField(default=True)
    create_at = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

class Subcategory(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(250)
    subcategory_image = fields.TextField()
    description = fields.TextField()
    category = fields.ForeignKeyField("models.Category", related_name=
                                      'subcategory',on_delete='CASCADE')
    is_active = fields.BooleanField(default=True)
    create_at = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

class Brand(Model):
    id = fields.IntField(pk = True)
    brand_name = fields.CharField(250)
    is_active = fields.BooleanField(default=True)
    create_at = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)
    
