import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class ViewedMatchs(SqlAlchemyBase):
    __tablename__ = 'viewed_matchs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=True)

    match_id = sqlalchemy.Column(sqlalchemy.Integer)
    user = relationship("User", back_populates="viewed_matchs")