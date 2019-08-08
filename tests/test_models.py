from match_games.models import Role, User, Store


class TestRole:
    def test_should_repr_return_repr_string(self):
        admin = Role(name='ADMIN')

        expected = "<Role(id=None, name='ADMIN')>"

        assert expected == repr(admin)


class TestUser:
    def test_should_repr_return_repr_string(self):
        admin = Role(name='ADMIN')

        barry = User(name='barry',
                     email='flash@dc.com',
                     password='eboard',
                     image='default.jpg')

        admin.users.append(barry)

        expected = f"<User(id=None, name='barry', role='{admin.name}')>"

        assert expected == repr(barry)


class TestStore:
    def test_should_repr_return_repr_string(self):
        shopb = Store(name='ShopB',
                      image='default.jpg')

        expected = f"<Store(id=None, name='ShopB')>"

        assert expected == repr(shopb)
