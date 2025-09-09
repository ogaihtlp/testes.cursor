from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, func, text
from typing import List, Dict, Any
from datetime import date
from collections import Counter
import re
from ..database import get_session
from ..models import MonthlyData, TravelData

router = APIRouter()

@router.get("/attendance-distribution")
def get_attendance_distribution(
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Distribuição por tipo de atendimento baseada nas observações"""
    
    # Buscar todas as observações dos dados mensais e viagens
    monthly_stmt = select(MonthlyData.observacoes).where(
        MonthlyData.usuario == usuario,
        MonthlyData.observacoes.isnot(None)
    )
    travel_stmt = select(TravelData.observacoes).where(
        TravelData.usuario == usuario,
        TravelData.observacoes.isnot(None)
    )
    
    monthly_obs = session.exec(monthly_stmt).all()
    travel_obs = session.exec(travel_stmt).all()
    
    # Categorizar baseado em palavras-chave
    categories = {"Remoto": 0, "Presencial": 0, "Híbrido": 0}
    
    all_observations = list(monthly_obs) + list(travel_obs)
    
    for obs in all_observations:
        if obs:
            obs_lower = obs.lower()
            if any(word in obs_lower for word in ['remoto', 'home office', 'online', 'virtual']):
                categories["Remoto"] += 1
            elif any(word in obs_lower for word in ['presencial', 'cliente', 'site', 'viagem']):
                categories["Presencial"] += 1
            else:
                categories["Híbrido"] += 1
    
    # Se não há dados categorizados, usar dados de viagem como presencial
    if sum(categories.values()) == 0:
        travel_count = session.exec(
            select(func.count(TravelData.id)).where(TravelData.usuario == usuario)
        ).first() or 0
        monthly_count = session.exec(
            select(func.count(MonthlyData.id)).where(MonthlyData.usuario == usuario)
        ).first() or 0
        
        categories["Presencial"] = travel_count
        categories["Remoto"] = max(0, monthly_count - travel_count)
    
    return {
        "labels": list(categories.keys()),
        "data": list(categories.values()),
        "total": sum(categories.values())
    }

@router.get("/hours-by-city")
def get_hours_by_city(
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Horas por cidade (Deslocamento x Atendimento)"""
    
    stmt = select(
        TravelData.cidade,
        func.sum(TravelData.tempo_deslocamento).label("total_deslocamento"),
        func.sum(TravelData.tempo_atendimento).label("total_atendimento")
    ).where(
        TravelData.usuario == usuario
    ).group_by(TravelData.cidade).order_by(
        func.sum(TravelData.tempo_deslocamento + TravelData.tempo_atendimento).desc()
    )
    
    results = session.exec(stmt).all()
    
    cities = []
    deslocamento = []
    atendimento = []
    
    for result in results:
        cities.append(result.cidade)
        deslocamento.append(float(result.total_deslocamento or 0))
        atendimento.append(float(result.total_atendimento or 0))
    
    return {
        "labels": cities,
        "datasets": [
            {
                "label": "Deslocamento (h)",
                "data": deslocamento,
                "backgroundColor": "#6c757d"
            },
            {
                "label": "Atendimento (h)", 
                "data": atendimento,
                "backgroundColor": "#2e7d59"
            }
        ],
        "total_hours": sum(deslocamento) + sum(atendimento)
    }

@router.get("/monthly-evolution")
def get_monthly_evolution(
    usuario: str = Query(..., description="Nome do usuário"),
    session: Session = Depends(get_session)
):
    """Evolução mensal de atendimentos"""
    
    # Definir ordem dos meses
    month_order = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    stmt = select(
        MonthlyData.mes,
        func.sum(MonthlyData.atendimentos).label("total_atendimentos"),
        func.sum(MonthlyData.horas_extras).label("total_horas_extras"),
        func.sum(MonthlyData.treinamentos).label("total_treinamentos")
    ).where(
        MonthlyData.usuario == usuario
    ).group_by(MonthlyData.mes)
    
    results = session.exec(stmt).all()
    
    # Organizar dados por mês
    monthly_data = {result.mes: result for result in results}
    
    labels = []
    atendimentos = []
    horas_extras = []
    treinamentos = []
    
    for mes in month_order:
        if mes in monthly_data:
            labels.append(mes[:3])  # Abreviação do mês
            data = monthly_data[mes]
            atendimentos.append(int(data.total_atendimentos or 0))
            horas_extras.append(float(data.total_horas_extras or 0))
            treinamentos.append(float(data.total_treinamentos or 0))
    
    return {
        "labels": labels,
        "datasets": [
            {
                "label": "Atendimentos",
                "data": atendimentos,
                "borderColor": "#2e7d59",
                "backgroundColor": "rgba(46, 125, 89, 0.1)",
                "tension": 0.4
            },
            {
                "label": "Horas Extras",
                "data": horas_extras,
                "borderColor": "#f39c12",
                "backgroundColor": "rgba(243, 156, 18, 0.1)",
                "tension": 0.4
            },
            {
                "label": "Treinamentos (h)",
                "data": treinamentos,
                "borderColor": "#3498db",
                "backgroundColor": "rgba(52, 152, 219, 0.1)",
                "tension": 0.4
            }
        ],
        "total_months": len(labels)
    }

@router.get("/top-clients")
def get_top_clients(
    usuario: str = Query(..., description="Nome do usuário"),
    limit: int = Query(5, description="Número máximo de clientes/projetos"),
    session: Session = Depends(get_session)
):
    """Top clientes/projetos baseado nas observações"""
    
    # Buscar observações de dados mensais e viagens
    monthly_stmt = select(MonthlyData.observacoes, MonthlyData.atendimentos).where(
        MonthlyData.usuario == usuario,
        MonthlyData.observacoes.isnot(None)
    )
    travel_stmt = select(TravelData.observacoes, TravelData.tempo_atendimento).where(
        TravelData.usuario == usuario,
        TravelData.observacoes.isnot(None)
    )
    
    monthly_results = session.exec(monthly_stmt).all()
    travel_results = session.exec(travel_stmt).all()
    
    # Extrair nomes de clientes/projetos das observações
    client_data = {}
    
    # Processar dados mensais
    for obs, atendimentos in monthly_results:
        if obs:
            # Extrair possíveis nomes de clientes (palavras capitalizadas, projetos, etc.)
            words = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', obs)
            project_words = re.findall(r'\b(?:projeto|cliente|empresa)\s+(\w+)', obs.lower())
            
            clients = words + [w.title() for w in project_words]
            
            for client in clients:
                if len(client) > 2:  # Filtrar palavras muito curtas
                    if client not in client_data:
                        client_data[client] = {"value": 0, "type": "atendimentos"}
                    client_data[client]["value"] += atendimentos or 0
    
    # Processar dados de viagem
    for obs, tempo_atendimento in travel_results:
        if obs:
            words = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', obs)
            project_words = re.findall(r'\b(?:projeto|cliente|empresa)\s+(\w+)', obs.lower())
            
            clients = words + [w.title() for w in project_words]
            
            for client in clients:
                if len(client) > 2:
                    if client not in client_data:
                        client_data[client] = {"value": 0, "type": "horas"}
                    client_data[client]["value"] += tempo_atendimento or 0
    
    # Se não há dados específicos, usar observações mais comuns
    if not client_data:
        all_obs = [obs for obs, _ in monthly_results] + [obs for obs, _ in travel_results]
        obs_counter = Counter([obs[:20] + "..." if len(obs) > 20 else obs for obs in all_obs if obs])
        
        for obs, count in obs_counter.most_common(limit):
            client_data[obs] = {"value": count, "type": "ocorrências"}
    
    # Ordenar e limitar
    sorted_clients = sorted(client_data.items(), key=lambda x: x[1]["value"], reverse=True)[:limit]
    
    labels = [client for client, _ in sorted_clients]
    data = [info["value"] for _, info in sorted_clients]
    
    return {
        "labels": labels,
        "data": data,
        "total": len(client_data)
    }