#!/bin/bash

echo "========================================"
echo "  Sistema de Gestão Pessoal - Servidor"
echo "========================================"
echo

echo "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python não encontrado!"
    echo "Instale Python 3.7+ e tente novamente."
    exit 1
fi

echo "Instalando dependências..."
pip3 install -r requirements.txt

echo
echo "Iniciando servidor..."
echo
echo "========================================"
echo "  Acesse: http://localhost:8000"
echo "  Para rede local, use o IP desta máquina"
echo "  Pressione Ctrl+C para parar"
echo "========================================"
echo

python3 server.py