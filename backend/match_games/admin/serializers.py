from marshmallow import fields, validate

from match_games import ma


class AuthenticationSerializer(ma.Schema):
    email = fields.String(required=True,
                          validate=[validate.Email(error='Email should be valid.')])
    password = fields.String(required=True,
                             validate=[validate.Length(min=3,
                                                       error='Password should be length equal or greater 3.')])


authentication_serializer = AuthenticationSerializer()
