import sqlalchemy
from .db_session import SqlAlchemyBase


class Session(SqlAlchemyBase):
    __tablename__ = 'sessions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    token = sqlalchemy.Column(sqlalchemy.String(128), nullable=False, unique=True)
    username = sqlalchemy.Column(sqlalchemy.String(20), nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    expires_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
