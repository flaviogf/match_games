from match_games.models import Role


class TestRole:
    def test_should_return_repr_string(self):
        admin = Role(name='ADMIN')

        expected = "<Role(id=None, name='ADMIN')>"

        assert expected == repr(admin)
