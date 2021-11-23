from marshmallow import fields, Schema
from .common.dataclasses import CamelcaseDataKey


class DiscountCodesSchema(CamelcaseDataKey, Schema):
    discount_code = fields.String()
    discount_value = fields.Int()


class UsersSchema(CamelcaseDataKey, Schema):
    username = fields.String()
    name = fields.String()
    email = fields.String()
    discount_code = fields.String()
