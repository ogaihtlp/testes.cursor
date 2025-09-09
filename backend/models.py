from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date
from enum import Enum

class MonthEnum(str, Enum):
    """Enum para os meses do ano"""
    JANEIRO = "Janeiro"
    FEVEREIRO = "Fevereiro"
    MARCO = "Março"
    ABRIL = "Abril"
    MAIO = "Maio"
    JUNHO = "Junho"
    JULHO = "Julho"
    AGOSTO = "Agosto"
    SETEMBRO = "Setembro"
    OUTUBRO = "Outubro"
    NOVEMBRO = "Novembro"
    DEZEMBRO = "Dezembro"

class MonthlyDataBase(SQLModel):
    """Modelo base para dados mensais"""
    mes: MonthEnum = Field(description="Mês de referência")
    atendimentos: int = Field(ge=0, description="Número de atendimentos")
    horas_extras: float = Field(ge=0, description="Horas em atividades de outros setores")
    treinamentos: float = Field(ge=0, description="Horas de treinamentos/capacitações online")
    tempo_off: float = Field(ge=0, description="Tempo Off - Viagens (horas)")
    observacoes: Optional[str] = Field(default=None, description="Observações opcionais")
    usuario: str = Field(description="Nome do usuário")

class MonthlyData(MonthlyDataBase, table=True):
    """Modelo de dados mensais na base"""
    __tablename__ = "monthly_data"
    
    id: Optional[int] = Field(default=None, primary_key=True)

class MonthlyDataCreate(MonthlyDataBase):
    """Modelo para criação de dados mensais"""
    pass

class MonthlyDataUpdate(SQLModel):
    """Modelo para atualização de dados mensais"""
    mes: Optional[MonthEnum] = None
    atendimentos: Optional[int] = Field(default=None, ge=0)
    horas_extras: Optional[float] = Field(default=None, ge=0)
    treinamentos: Optional[float] = Field(default=None, ge=0)
    tempo_off: Optional[float] = Field(default=None, ge=0)
    observacoes: Optional[str] = None

class TravelDataBase(SQLModel):
    """Modelo base para dados de viagem"""
    cidade: str = Field(description="Cidade de destino")
    tempo_deslocamento: float = Field(ge=0, description="Tempo de deslocamento em horas")
    tempo_atendimento: float = Field(ge=0, description="Tempo em atendimento em horas")
    data_inicio: date = Field(description="Data de início da viagem")
    data_fim: date = Field(description="Data de término da viagem")
    observacoes: Optional[str] = Field(default=None, description="Observações opcionais")
    usuario: str = Field(description="Nome do usuário")

class TravelData(TravelDataBase, table=True):
    """Modelo de dados de viagem na base"""
    __tablename__ = "travel_data"
    
    id: Optional[int] = Field(default=None, primary_key=True)

class TravelDataCreate(TravelDataBase):
    """Modelo para criação de dados de viagem"""
    pass

class TravelDataUpdate(SQLModel):
    """Modelo para atualização de dados de viagem"""
    cidade: Optional[str] = None
    tempo_deslocamento: Optional[float] = Field(default=None, ge=0)
    tempo_atendimento: Optional[float] = Field(default=None, ge=0)
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    observacoes: Optional[str] = None

class StatsResponse(SQLModel):
    """Modelo para resposta de estatísticas"""
    total_atendimentos: int
    total_horas_extras: float
    total_treinamentos: float
    total_viagens: int
    total_deslocamento: float
    total_atendimento_viagem: float