@echo off
echo ========================================
echo   Sistema de Gestao Pessoal - Servidor
echo ========================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.7+ e tente novamente.
    pause
    exit /b 1
)

echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Iniciando servidor...
echo.
echo ========================================
echo   Acesse: http://localhost:8000
echo   Para rede local, use o IP desta maquina
echo   Pressione Ctrl+C para parar
echo ========================================
echo.

python server.py
pause