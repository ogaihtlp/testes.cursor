from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, func
from ..database import get_session
from ..models import MonthlyData, TravelData, StatsResponse

router = APIRouter()

@router.get("/", response_model=StatsResponse)
def get_user_stats(
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Buscar estatísticas consolidadas do usuário"""
    
    # Estatísticas dos dados mensais
    monthly_stats = session.exec(
        select(
            func.coalesce(func.sum(MonthlyData.atendimentos), 0).label("total_atendimentos"),
            func.coalesce(func.sum(MonthlyData.horas_extras), 0.0).label("total_horas_extras"),
            func.coalesce(func.sum(MonthlyData.treinamentos), 0.0).label("total_treinamentos")
        ).where(MonthlyData.usuario == usuario)
    ).first()
    
    # Estatísticas dos dados de viagem
    travel_stats = session.exec(
        select(
            func.count(TravelData.id).label("total_viagens"),
            func.coalesce(func.sum(TravelData.tempo_deslocamento), 0.0).label("total_deslocamento"),
            func.coalesce(func.sum(TravelData.tempo_atendimento), 0.0).label("total_atendimento_viagem")
        ).where(TravelData.usuario == usuario)
    ).first()
    
    return StatsResponse(
        total_atendimentos=monthly_stats.total_atendimentos if monthly_stats else 0,
        total_horas_extras=monthly_stats.total_horas_extras if monthly_stats else 0.0,
        total_treinamentos=monthly_stats.total_treinamentos if monthly_stats else 0.0,
        total_viagens=travel_stats.total_viagens if travel_stats else 0,
        total_deslocamento=travel_stats.total_deslocamento if travel_stats else 0.0,
        total_atendimento_viagem=travel_stats.total_atendimento_viagem if travel_stats else 0.0
    )