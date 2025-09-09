# 🐍 Guia de Ambientes Python - Sistema de Gestão Pessoal

## ❓ **O que é um Ambiente Virtual (venv)?**

Um ambiente virtual é um **espaço isolado** onde você pode instalar bibliotecas Python específicas para um projeto, sem interferir com outras aplicações ou com o sistema.

## ✅ **Por que usar venv?**

### 🔐 **Isolamento**
- Cada projeto tem suas próprias dependências
- Não há conflito entre versões diferentes
- O sistema Python permanece limpo

### 🎯 **Controle**
- Versões específicas das bibliotecas
- Fácil de replicar em outros computadores
- Backup simples do ambiente

### 🧹 **Limpeza**
- Fácil de deletar sem afetar o sistema
- Reinstalação rápida se necessário
- Não "suja" o Python global

## 🚀 **Como Configurar**

### **Linux/Mac**
```bash
# 1. Criar ambiente virtual
python3 -m venv venv

# 2. Ativar
source venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar projeto
python run.py

# 5. Desativar (quando terminar)
deactivate
```

### **Windows**
```cmd
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar
venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar projeto
python run.py

# 5. Desativar (quando terminar)
deactivate
```

## 🤖 **Configuração Automática**

### **Usar os Scripts Prontos:**

**Linux/Mac:**
```bash
./setup_venv.sh
```

**Windows:**
```cmd
setup_venv.bat
```

## 🔍 **Como Identificar se está no venv?**

Quando o ambiente virtual está ativo, você verá `(venv)` no início do seu prompt:

```bash
# Sem venv
usuario@computador:~/projeto$ 

# Com venv ativo
(venv) usuario@computador:~/projeto$ 
```

## 📁 **Estrutura de Arquivos**

```
projeto/
├── venv/                 # Ambiente virtual (não versionar!)
│   ├── bin/ (ou Scripts/)
│   ├── lib/
│   └── pyvenv.cfg
├── backend/
├── requirements.txt
├── setup_venv.sh
└── ...
```

## ⚠️ **Importante: .gitignore**

**NUNCA** versione a pasta `venv/` no Git:

```gitignore
# Ambiente virtual
venv/
.venv/
env/
ENV/
```

## 🆘 **Solução de Problemas**

### **Python não encontrado**
```bash
# Verificar instalação
python3 --version
# ou
python --version

# Se não tiver, instalar Python primeiro
```

### **Permissão negada (Linux/Mac)**
```bash
# Dar permissão ao script
chmod +x setup_venv.sh
```

### **Erro de política de execução (Windows)**
```powershell
# No PowerShell como Administrador:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **venv não funciona**
```bash
# Instalar módulo venv
sudo apt install python3-venv  # Ubuntu/Debian
# ou
brew install python3           # macOS
```

## 🔄 **Workflow Diário**

### **Primeira vez:**
1. `./setup_venv.sh` (ou `setup_venv.bat`)
2. `python run.py`

### **Próximas vezes:**
1. `source venv/bin/activate` (ativar venv)
2. `python run.py`
3. `deactivate` (quando terminar)

## 📦 **Gerenciamento de Dependências**

### **Adicionar nova biblioteca:**
```bash
# Com venv ativo
pip install nova-biblioteca

# Atualizar requirements.txt
pip freeze > requirements.txt
```

### **Recriar ambiente:**
```bash
# Deletar ambiente atual
rm -rf venv/

# Recriar
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

💡 **Dica:** Use sempre ambiente virtual para projetos Python. É uma boa prática profissional!