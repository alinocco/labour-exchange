from datetime import datetime
import sqlalchemy
from .base import metadata

users = sqlalchemy.Table(
    "users", 
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("is_company", sqlalchemy.Boolean),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, default=datetime.utcnow),
    sqlalchemy.Column("changed_date", sqlalchemy.DateTime, default=datetime.utcnow),
    )