from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from typing import List
from datetime import date
from ..database import get_session
from ..models import TravelData, TravelDataCreate, TravelDataUpdate

router = APIRouter()

@router.get("/", response_model=List[TravelData])
def get_travel_data(
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Buscar todos os dados de viagem de um usuário"""
    statement = select(TravelData).where(TravelData.usuario == usuario).order_by(TravelData.data_inicio.desc())
    travel_data = session.exec(statement).all()
    return travel_data

@router.get("/{travel_id}", response_model=TravelData)
def get_travel_data_by_id(
    travel_id: int,
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Buscar dados de viagem por ID"""
    statement = select(TravelData).where(
        TravelData.id == travel_id,
        TravelData.usuario == usuario
    )
    travel_data = session.exec(statement).first()
    
    if not travel_data:
        raise HTTPException(status_code=404, detail="Dados de viagem não encontrados")
    
    return travel_data

@router.post("/", response_model=TravelData)
def create_travel_data(
    travel_data: TravelDataCreate,
    session: Session = Depends(get_session)
):
    """Criar novo registro de viagem"""
    
    # Validar datas
    if travel_data.data_fim < travel_data.data_inicio:
        raise HTTPException(
            status_code=400,
            detail="A data de término não pode ser anterior à data de início"
        )
    
    # Criar novo registro
    db_travel_data = TravelData.model_validate(travel_data)
    session.add(db_travel_data)
    session.commit()
    session.refresh(db_travel_data)
    
    return db_travel_data

@router.put("/{travel_id}", response_model=TravelData)
def update_travel_data(
    travel_id: int,
    travel_update: TravelDataUpdate,
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Atualizar dados de viagem"""
    statement = select(TravelData).where(
        TravelData.id == travel_id,
        TravelData.usuario == usuario
    )
    db_travel_data = session.exec(statement).first()
    
    if not db_travel_data:
        raise HTTPException(status_code=404, detail="Dados de viagem não encontrados")
    
    # Atualizar campos fornecidos
    travel_update_data = travel_update.model_dump(exclude_unset=True)
    
    # Validar datas se ambas estiverem sendo atualizadas
    data_inicio = travel_update_data.get('data_inicio', db_travel_data.data_inicio)
    data_fim = travel_update_data.get('data_fim', db_travel_data.data_fim)
    
    if data_fim < data_inicio:
        raise HTTPException(
            status_code=400,
            detail="A data de término não pode ser anterior à data de início"
        )
    
    for field, value in travel_update_data.items():
        setattr(db_travel_data, field, value)
    
    session.add(db_travel_data)
    session.commit()
    session.refresh(db_travel_data)
    
    return db_travel_data

@router.delete("/{travel_id}")
def delete_travel_data(
    travel_id: int,
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Excluir dados de viagem"""
    statement = select(TravelData).where(
        TravelData.id == travel_id,
        TravelData.usuario == usuario
    )
    db_travel_data = session.exec(statement).first()
    
    if not db_travel_data:
        raise HTTPException(status_code=404, detail="Dados de viagem não encontrados")
    
    session.delete(db_travel_data)
    session.commit()
    
    return {"message": "Registro de viagem excluído com sucesso"}