from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from typing import List, Optional
from ..database import get_session
from ..models import MonthlyData, MonthlyDataCreate, MonthlyDataUpdate

router = APIRouter()

@router.get("/", response_model=List[MonthlyData])
def get_monthly_data(
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Buscar todos os dados mensais de um usuário"""
    statement = select(MonthlyData).where(MonthlyData.usuario == usuario)
    monthly_data = session.exec(statement).all()
    return monthly_data

@router.get("/{monthly_id}", response_model=MonthlyData)
def get_monthly_data_by_id(
    monthly_id: int,
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Buscar dados mensais por ID"""
    statement = select(MonthlyData).where(
        MonthlyData.id == monthly_id,
        MonthlyData.usuario == usuario
    )
    monthly_data = session.exec(statement).first()
    
    if not monthly_data:
        raise HTTPException(status_code=404, detail="Dados mensais não encontrados")
    
    return monthly_data

@router.post("/", response_model=MonthlyData)
def create_monthly_data(
    monthly_data: MonthlyDataCreate,
    session: Session = Depends(get_session)
):
    """Criar novo registro de dados mensais"""
    
    # Verificar se já existe registro para o mesmo mês/usuário
    statement = select(MonthlyData).where(
        MonthlyData.mes == monthly_data.mes,
        MonthlyData.usuario == monthly_data.usuario
    )
    existing_data = session.exec(statement).first()
    
    if existing_data:
        raise HTTPException(
            status_code=400, 
            detail=f"Já existe registro para {monthly_data.mes} do usuário {monthly_data.usuario}"
        )
    
    # Criar novo registro
    db_monthly_data = MonthlyData.model_validate(monthly_data)
    session.add(db_monthly_data)
    session.commit()
    session.refresh(db_monthly_data)
    
    return db_monthly_data

@router.put("/{monthly_id}", response_model=MonthlyData)
def update_monthly_data(
    monthly_id: int,
    monthly_update: MonthlyDataUpdate,
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Atualizar dados mensais"""
    statement = select(MonthlyData).where(
        MonthlyData.id == monthly_id,
        MonthlyData.usuario == usuario
    )
    db_monthly_data = session.exec(statement).first()
    
    if not db_monthly_data:
        raise HTTPException(status_code=404, detail="Dados mensais não encontrados")
    
    # Atualizar campos fornecidos
    monthly_update_data = monthly_update.model_dump(exclude_unset=True)
    for field, value in monthly_update_data.items():
        setattr(db_monthly_data, field, value)
    
    session.add(db_monthly_data)
    session.commit()
    session.refresh(db_monthly_data)
    
    return db_monthly_data

@router.delete("/{monthly_id}")
def delete_monthly_data(
    monthly_id: int,
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Excluir dados mensais"""
    statement = select(MonthlyData).where(
        MonthlyData.id == monthly_id,
        MonthlyData.usuario == usuario
    )
    db_monthly_data = session.exec(statement).first()
    
    if not db_monthly_data:
        raise HTTPException(status_code=404, detail="Dados mensais não encontrados")
    
    session.delete(db_monthly_data)
    session.commit()
    
    return {"message": "Registro excluído com sucesso"}