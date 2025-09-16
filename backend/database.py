from sqlmodel import SQLModel, create_engine
from typing import Optional
import os

# Configuração do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./gestao.db")

# Engine do banco
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Log de queries SQL (remover em produção)
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

def create_db_and_tables():
    """Cria o banco de dados e todas as tabelas"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Cria uma nova sessão de banco de dados"""
    from sqlmodel import Session
    with Session(engine) as session:
        yield session