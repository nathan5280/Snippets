from auth import auth_db


class User(auth_db.Model):
    __tablename__ = 'users'

    id = auth_db.Column(auth_db.Integer, primary_key=True)
    name = auth_db.Column(auth_db.String(20), unique=True)
    password = auth_db.Column(auth_db.String(20))

    def save(self):
        auth_db.session.add(self)
        auth_db.session.commit()

    @classmethod
    def find(cls, *, name: str = None, id_: int = None):
        assert name or id

        if name:
            return cls.query.filter(cls.name == name).one_or_none()

        if id_:
            return cls.query.filter(cls.id == id_).one_or_none()

    @classmethod
    def list(cls):
        users = cls.query.all()

        return users
