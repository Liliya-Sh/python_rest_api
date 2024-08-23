from marshmallow import Schema, fields


class OrderCreateDtoSchema(Schema):
    product_ids = fields.List(fields.Str(), required=True)


class OrderSchema(Schema):
    id = fields.String()
    product_ids = fields.List(fields.Str())
    total = fields.Float()


class OrderGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
