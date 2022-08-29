from datetime import datetime
import sqlalchemy
from .base import metadata

jobs = sqlalchemy.Table(
    "jobs", 
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("salary_from", sqlalchemy.Integer),
    sqlalchemy.Column("salary_to", sqlalchemy.Integer),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, default=datetime.utcnow),
    sqlalchemy.Column("changed_date", sqlalchemy.DateTime, default=datetime.utcnow),
    )