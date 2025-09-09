# 🚀 Início Rápido - Sistema de Gestão Pessoal

## ✅ **Método Recomendado: Com Ambiente Virtual**

### Linux/Mac
```bash
# Configuração automática
chmod +x setup_venv.sh
./setup_venv.sh

# Ou manual:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Windows
```bash
# Configuração automática
setup_venv.bat

# Ou manual:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## ⚠️ **Método Alternativo: Sem Ambiente Virtual**

### 1️⃣ Instalar
```bash
python3 -m pip install --break-system-packages -r requirements.txt
```

### 2️⃣ Executar
```bash
python3 run.py
```

### 3️⃣ Usar
1. Abrir `controle de dados.html` no navegador
2. Digite seu nome na configuração inicial
3. Começar a usar! 

## 📊 Interface

- **🟢 API conectada**: Dados salvos no banco de dados
- **🔴 API desconectada**: Dados salvos no navegador (localStorage)

## 🔗 URLs Úteis

- **Frontend**: `controle de dados.html` (abrir no navegador)
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## ❗ Problemas Comuns

### API não conecta
```bash
# Verificar se o servidor está rodando
curl http://localhost:8000/health

# Se não estiver, iniciar novamente
python3 run.py
```

### Erro de dependências
```bash
# Em ambientes restritivos, usar:
python3 -m pip install --user -r requirements.txt
# ou
python3 -m pip install --break-system-packages -r requirements.txt
```

---

✅ **Sistema funcionando?** O indicador no cabeçalho mostra se a API está conectada!