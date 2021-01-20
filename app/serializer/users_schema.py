from app.models import ma, User


class UserSchema(ma.SQLAlchemySchema):
    """ Serializer to users """
    class Meta:
        """ From where fields will come """
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    is_admin = ma.auto_field()
