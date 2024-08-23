from marshmallow import Schema, fields, validates, ValidationError


class ProductSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

    @validates('name')
    def validate_name(self, value):
        """Проверяем, чтобы наименование продукта было указано"""
        if not value.strip():
            raise ValidationError("Наименование товара не может быть пустым.")


class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
