#!/bin/bash
# Script para configurar ambiente virtual

echo "🐍 Configurando ambiente virtual Python..."

# Verificar se python3 está disponível
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale primeiro."
    exit 1
fi

# Criar ambiente virtual
echo "📁 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
echo "⚡ Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar pip
echo "📦 Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

echo "✅ Ambiente virtual configurado com sucesso!"
echo ""
echo "Para ativar o ambiente virtual no futuro:"
echo "  source venv/bin/activate"
echo ""
echo "Para executar o projeto:"
echo "  python run.py"
echo ""
echo "Para desativar o ambiente virtual:"
echo "  deactivate"