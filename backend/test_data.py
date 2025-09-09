"""
Script para criar dados de teste no sistema
"""

from sqlmodel import Session, create_engine
from database import engine
from models import MonthlyData, TravelData, MonthEnum
from datetime import date

def create_test_data():
    """Criar dados de teste para demonstração"""
    
    with Session(engine) as session:
        print("📝 Criando dados de teste...")
        
        # Dados mensais de exemplo
        monthly_test_data = [
            MonthlyData(
                mes=MonthEnum.JANEIRO,
                atendimentos=25,
                horas_extras=12.5,
                treinamentos=8.0,
                tempo_off=4.0,
                observacoes="Cliente ABC Corp - projeto remoto",
                usuario="João Silva"
            ),
            MonthlyData(
                mes=MonthEnum.FEVEREIRO,
                atendimentos=32,
                horas_extras=15.0,
                treinamentos=6.0,
                tempo_off=8.0,
                observacoes="Projeto Beta - trabalho híbrido",
                usuario="João Silva"
            ),
            MonthlyData(
                mes=MonthEnum.MARCO,
                atendimentos=28,
                horas_extras=10.0,
                treinamentos=12.0,
                tempo_off=6.0,
                observacoes="Cliente TechCorp - atendimento presencial",
                usuario="João Silva"
            ),
            MonthlyData(
                mes=MonthEnum.ABRIL,
                atendimentos=35,
                horas_extras=18.0,
                treinamentos=4.0,
                tempo_off=10.0,
                observacoes="Empresa Delta - home office",
                usuario="João Silva"
            ),
            MonthlyData(
                mes=MonthEnum.MAIO,
                atendimentos=29,
                horas_extras=14.0,
                treinamentos=9.0,
                tempo_off=5.0,
                observacoes="Cliente ABC Corp - continuação remoto",
                usuario="João Silva"
            ),
            MonthlyData(
                mes=MonthEnum.JUNHO,
                atendimentos=31,
                horas_extras=16.0,
                treinamentos=7.0,
                tempo_off=12.0,
                observacoes="Projeto Gamma - atendimento presencial",
                usuario="João Silva"
            )
        ]
        
        # Dados de viagem de exemplo
        travel_test_data = [
            TravelData(
                cidade="São Paulo",
                tempo_deslocamento=4.0,
                tempo_atendimento=16.0,
                data_inicio=date(2024, 1, 15),
                data_fim=date(2024, 1, 17),
                observacoes="Cliente ABC Corp - reunião estratégica",
                usuario="João Silva"
            ),
            TravelData(
                cidade="Rio de Janeiro",
                tempo_deslocamento=2.5,
                tempo_atendimento=14.0,
                data_inicio=date(2024, 2, 8),
                data_fim=date(2024, 2, 10),
                observacoes="Empresa TechCorp - workshop",
                usuario="João Silva"
            ),
            TravelData(
                cidade="Belo Horizonte",
                tempo_deslocamento=3.0,
                tempo_atendimento=12.0,
                data_inicio=date(2024, 3, 5),
                data_fim=date(2024, 3, 7),
                observacoes="Projeto Gamma - implementação",
                usuario="João Silva"
            ),
            TravelData(
                cidade="São Paulo",
                tempo_deslocamento=4.0,
                tempo_atendimento=20.0,
                data_inicio=date(2024, 4, 12),
                data_fim=date(2024, 4, 15),
                observacoes="Cliente ABC Corp - fase 2",
                usuario="João Silva"
            ),
            TravelData(
                cidade="Brasília",
                tempo_deslocamento=5.0,
                tempo_atendimento=18.0,
                data_inicio=date(2024, 5, 20),
                data_fim=date(2024, 5, 23),
                observacoes="Empresa Delta - consultoria",
                usuario="João Silva"
            ),
            TravelData(
                cidade="Rio de Janeiro",
                tempo_deslocamento=2.0,
                tempo_atendimento=10.0,
                data_inicio=date(2024, 6, 10),
                data_fim=date(2024, 6, 12),
                observacoes="Cliente TechCorp - treinamento",
                usuario="João Silva"
            )
        ]
        
        # Adicionar dados mensais
        for data in monthly_test_data:
            session.add(data)
        
        # Adicionar dados de viagem
        for data in travel_test_data:
            session.add(data)
        
        session.commit()
        
        print("✅ Dados de teste criados com sucesso!")
        print(f"📊 {len(monthly_test_data)} registros mensais")
        print(f"✈️ {len(travel_test_data)} registros de viagem")
        print("👤 Usuário de teste: João Silva")

if __name__ == "__main__":
    create_test_data()