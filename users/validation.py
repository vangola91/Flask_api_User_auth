from marshmallow import Schema, fields, validate


class CreateSignupInputSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=4))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


class CreateLoginInputSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


class CreateResetPasswordEmailSendInputSchema(Schema):
    email = fields.Email(required=True)


class ResetPasswordInputSchema(Schema):
    password = fields.Str(required=True, validate=validate.Length(min=6))
