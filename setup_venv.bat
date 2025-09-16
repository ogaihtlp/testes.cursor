@echo off
REM Script para configurar ambiente virtual no Windows

echo 🐍 Configurando ambiente virtual Python...

REM Verificar se python está disponível
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado. Instale primeiro.
    pause
    exit /b 1
)

REM Criar ambiente virtual
echo 📁 Criando ambiente virtual...
python -m venv venv

REM Ativar ambiente virtual
echo ⚡ Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Atualizar pip
echo 📦 Atualizando pip...
python -m pip install --upgrade pip

REM Instalar dependências
echo 📚 Instalando dependências...
pip install -r requirements.txt

echo ✅ Ambiente virtual configurado com sucesso!
echo.
echo Para ativar o ambiente virtual no futuro:
echo   venv\Scripts\activate.bat
echo.
echo Para executar o projeto:
echo   python run.py
echo.
echo Para desativar o ambiente virtual:
echo   deactivate
echo.
pause