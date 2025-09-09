#!/bin/bash

# Script para testar o dashboard analítico
echo "🧪 Teste do Dashboard Analítico"
echo "================================"

# Configurações
API_BASE="http://localhost:8000"
USUARIO="João Silva"
USUARIO_ENCODED="Jo%C3%A3o%20Silva"

# Testar saúde da API
echo "🔍 Testando conexão com a API..."
HEALTH_RESPONSE=$(curl -s "$API_BASE/health" 2>/dev/null)

if [ $? -eq 0 ] && [[ $HEALTH_RESPONSE == *"healthy"* ]]; then
    echo "✅ API está funcionando"
else
    echo "❌ API não está funcionando"
    echo "💡 Para iniciar a API execute: python3 run.py"
    exit 1
fi

echo ""

# Testar endpoints analíticos
echo "📊 Testando endpoints analíticos para usuário: $USUARIO"
echo "--------------------------------------------------------"

# Teste 1: Distribuição por Tipo de Atendimento
echo "🥧 Distribuição por Tipo de Atendimento:"
ATTENDANCE_DATA=$(curl -s "$API_BASE/api/analytics/attendance-distribution?usuario=$USUARIO_ENCODED")
if [[ $ATTENDANCE_DATA == *"total"* ]]; then
    TOTAL=$(echo $ATTENDANCE_DATA | grep -o '"total":[0-9]*' | cut -d':' -f2)
    echo "   ✅ Total de registros: $TOTAL"
    echo "   📊 Dados: $ATTENDANCE_DATA"
else
    echo "   ❌ Erro ao buscar dados"
fi
echo ""

# Teste 2: Horas por Cidade
echo "🏙️ Horas por Cidade:"
CITY_DATA=$(curl -s "$API_BASE/api/analytics/hours-by-city?usuario=$USUARIO_ENCODED")
if [[ $CITY_DATA == *"total_hours"* ]]; then
    TOTAL_HOURS=$(echo $CITY_DATA | grep -o '"total_hours":[0-9.]*' | cut -d':' -f2)
    echo "   ✅ Total de horas: ${TOTAL_HOURS}h"
    echo "   🏢 Cidades encontradas no JSON"
else
    echo "   ❌ Erro ao buscar dados"
fi
echo ""

# Teste 3: Evolução Mensal
echo "📈 Evolução Mensal:"
EVOLUTION_DATA=$(curl -s "$API_BASE/api/analytics/monthly-evolution?usuario=$USUARIO_ENCODED")
if [[ $EVOLUTION_DATA == *"total_months"* ]]; then
    TOTAL_MONTHS=$(echo $EVOLUTION_DATA | grep -o '"total_months":[0-9]*' | cut -d':' -f2)
    echo "   ✅ Meses com dados: $TOTAL_MONTHS"
    echo "   📅 Evolução temporal disponível"
else
    echo "   ❌ Erro ao buscar dados"
fi
echo ""

# Teste 4: Top Clientes
echo "🏢 Top Clientes/Projetos:"
CLIENTS_DATA=$(curl -s "$API_BASE/api/analytics/top-clients?usuario=$USUARIO_ENCODED")
if [[ $CLIENTS_DATA == *"total"* ]]; then
    CLIENTS_TOTAL=$(echo $CLIENTS_DATA | grep -o '"total":[0-9]*' | cut -d':' -f2)
    echo "   ✅ Clientes identificados: $CLIENTS_TOTAL"
    echo "   👥 Ranking disponível"
else
    echo "   ❌ Erro ao buscar dados"
fi
echo ""

# Verificar dados básicos
echo "📋 Verificando dados básicos:"
MONTHLY_COUNT=$(curl -s "$API_BASE/api/monthly/?usuario=$USUARIO_ENCODED" | grep -o '"id":' | wc -l)
TRAVEL_COUNT=$(curl -s "$API_BASE/api/travel/?usuario=$USUARIO_ENCODED" | grep -o '"id":' | wc -l)

echo "   📅 Registros mensais: $MONTHLY_COUNT"
echo "   ✈️ Registros de viagem: $TRAVEL_COUNT"
echo ""

# Status final
echo "🎉 Teste concluído!"
echo ""
echo "📊 Para visualizar os gráficos:"
echo "1. Abra 'controle de dados.html' no navegador"
echo "2. Digite '$USUARIO' como nome"
echo "3. Clique na aba '📊 Dashboard'"
echo ""
echo "🔗 Documentação completa da API:"
echo "   http://localhost:8000/docs"
echo ""
echo "📖 Guias disponíveis:"
echo "   - README.md (visão geral)"
echo "   - DASHBOARD_GUIDE.md (guia do dashboard)"
echo "   - QUICK_START.md (início rápido)"