# 📊 Sistema de Gestão Pessoal

Sistema completo para controle de dados mensais e registros de viagem, com frontend responsivo e backend API REST.

## 🚀 Funcionalidades

### 📋 Dados Mensais
- Controle de atendimentos mensais
- Registro de horas em atividades de outros setores
- Controle de treinamentos e capacitações online
- Registro de tempo off para viagens
- Observações personalizadas

### ✈️ Registros de Viagem
- Cadastro de destinos de viagem
- Controle de tempo de deslocamento
- Registro de horas em atendimento
- Controle de período da viagem (início/fim)
- Observações sobre cada viagem

### 📊 Dashboard Analítico Avançado
- **🥧 Distribuição por Tipo de Atendimento** - Gráfico donut com categorização automática (remoto/presencial/híbrido)
- **🏙️ Horas por Cidade** - Barras empilhadas mostrando deslocamento vs atendimento
- **📈 Evolução Mensal** - Gráficos de linha com trends temporais
- **🏢 Top Clientes/Projetos** - Ranking baseado nas observações
- Gráficos interativos com Chart.js
- Atualização automática em tempo real
- Design responsivo para mobile e desktop

### 📊 Dashboard e Relatórios
- Estatísticas consolidadas em tempo real
- Totalizadores de atendimentos, horas extras e treinamentos
- Métricas de viagens e deslocamentos
- Exportação de dados para Excel
- Interface responsiva e moderna

## 🛠️ Tecnologias

### Frontend
- **HTML5** com design responsivo
- **JavaScript vanilla** para interatividade
- **Chart.js** para gráficos interativos e dashboard
- **CSS3** com gradientes e animações
- **SheetJS (xlsx)** para exportação Excel
- **LocalStorage** para persistência local

### Backend
- **FastAPI** - Framework web moderno e rápido
- **SQLModel** - ORM baseado em SQLAlchemy e Pydantic
- **SQLite** - Banco de dados embutido
- **Uvicorn** - Servidor ASGI

## 🔧 Instalação e Execução

### Método Recomendado: Ambiente Virtual

#### Linux/Mac
```bash
# Configuração automática
./setup_venv.sh

# Executar (com venv ativado)
python run.py
```

#### Windows
```bash
# Configuração automática
setup_venv.bat

# Executar (com venv ativado)
python run.py
```

#### Manual
```bash
# 1. Criar ambiente virtual
python3 -m venv venv

# 2. Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar
python run.py
```

### Método Alternativo: Sem Ambiente Virtual
```bash
# 1. Instalar dependências globalmente
python3 -m pip install --break-system-packages -r requirements.txt

# 2. Executar o backend
python3 run.py
# ou
python3 -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Acessar a Aplicação
- **Frontend**: Abrir `controle de dados.html` no navegador
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### 4. Testar Dados (Opcional)
```bash
# Criar dados de teste no banco
python3 -c "from backend.test_data import create_test_data; create_test_data()"
```

## 📡 API Endpoints

### Dados Mensais
- `GET /api/monthly/` - Listar dados mensais
- `POST /api/monthly/` - Criar novo registro mensal
- `PUT /api/monthly/{id}` - Atualizar registro mensal
- `DELETE /api/monthly/{id}` - Excluir registro mensal

### Registros de Viagem
- `GET /api/travel/` - Listar registros de viagem
- `POST /api/travel/` - Criar novo registro de viagem
- `PUT /api/travel/{id}` - Atualizar registro de viagem
- `DELETE /api/travel/{id}` - Excluir registro de viagem

### Estatísticas
- `GET /api/stats/` - Obter estatísticas consolidadas

### Analytics (Gráficos)
- `GET /api/analytics/attendance-distribution` - Distribuição por tipo de atendimento
- `GET /api/analytics/hours-by-city` - Horas por cidade (deslocamento + atendimento)
- `GET /api/analytics/monthly-evolution` - Evolução mensal de métricas
- `GET /api/analytics/top-clients` - Top clientes/projetos baseado em observações

## 💾 Estrutura do Banco de Dados

### Tabela `monthly_data`
- `id`: Identificador único
- `mes`: Mês de referência (enum)
- `atendimentos`: Número de atendimentos
- `horas_extras`: Horas em outros setores
- `treinamentos`: Horas de treinamentos
- `tempo_off`: Tempo off em viagens
- `observacoes`: Observações opcionais
- `usuario`: Nome do usuário

### Tabela `travel_data`
- `id`: Identificador único
- `cidade`: Cidade de destino
- `tempo_deslocamento`: Horas de deslocamento
- `tempo_atendimento`: Horas em atendimento
- `data_inicio`: Data de início da viagem
- `data_fim`: Data de término da viagem
- `observacoes`: Observações opcionais
- `usuario`: Nome do usuário

## ✅ Status do Projeto

### Implementado
- [x] Backend FastAPI completo com SQLModel
- [x] Frontend integrado com API REST
- [x] CRUD completo para dados mensais e viagens
- [x] **Dashboard analítico completo com 4 gráficos interativos**
- [x] **Endpoints de analytics para agregação de dados**
- [x] **Gráficos Chart.js responsivos e modernos**
- [x] Estatísticas em tempo real
- [x] Banco de dados SQLite com migrações automáticas
- [x] Indicador de conexão API/offline
- [x] Fallback para localStorage quando API não disponível
- [x] Interface responsiva e moderna
- [x] Exportação para Excel
- [x] Documentação automática da API

### 🎯 Próximos Passos

- [ ] Sistema de autenticação/autorização JWT
- [ ] Relatórios avançados com gráficos
- [ ] Dashboard analítico interativo
- [ ] Deploy em produção (Docker + Nginx)
- [ ] Testes automatizados (pytest + frontend tests)
- [ ] Notificações e lembretes
- [ ] Import de dados via CSV/Excel
- [ ] Backup automático dos dados

## 📝 Licença

Este projeto é de uso pessoal e educacional.

---

⚡ **Desenvolvido com FastAPI + SQLModel para máxima performance e facilidade de uso!**