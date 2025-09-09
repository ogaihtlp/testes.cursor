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
                observacoes="Início do projeto Alpha",
                usuario="João Silva"
            ),
            MonthlyData(
                mes=MonthEnum.FEVEREIRO,
                atendimentos=32,
                horas_extras=15.0,
                treinamentos=6.0,
                tempo_off=8.0,
                observacoes="Implementação da fase 2",
                usuario="João Silva"
            ),
            MonthlyData(
                mes=MonthEnum.MARCO,
                atendimentos=28,
                horas_extras=10.0,
                treinamentos=12.0,
                tempo_off=6.0,
                observacoes="Treinamento em novas tecnologias",
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
                observacoes="Reunião com cliente ABC Corp",
                usuario="João Silva"
            ),
            TravelData(
                cidade="Brasília",
                tempo_deslocamento=6.0,
                tempo_atendimento=12.0,
                data_inicio=date(2024, 2, 8),
                data_fim=date(2024, 2, 10),
                observacoes="Workshop de capacitação",
                usuario="João Silva"
            ),
            TravelData(
                cidade="Belo Horizonte",
                tempo_deslocamento=3.0,
                tempo_atendimento=20.0,
                data_inicio=date(2024, 3, 5),
                data_fim=date(2024, 3, 8),
                observacoes="Implementação do sistema XYZ",
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