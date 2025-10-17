# 🌐 Sistema de Gestão Pessoal - Configuração para Rede Local

Este guia explica como configurar o sistema para funcionar em outros computadores da mesma rede.

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Conexão de rede local (WiFi ou cabo)

## 🚀 Instalação e Configuração

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o Servidor

```bash
python server.py
```

### 3. Acessar o Sistema

#### No computador principal (servidor):
- Acesse: `http://localhost:8000`

#### Em outros computadores da rede:
- Descubra o IP da máquina servidor:
  - Windows: `ipconfig`
  - Linux/Mac: `ifconfig` ou `ip addr`
- Acesse: `http://[IP_DA_MAQUINA]:8000`
- Exemplo: `http://192.168.1.100:8000`

## 🔧 Configuração de Rede

### Descobrir o IP da Máquina

#### Windows:
```cmd
ipconfig
```
Procure por "Endereço IPv4" na seção da sua conexão de rede.

#### Linux/Mac:
```bash
ifconfig
```
Procure por "inet" na seção da sua interface de rede.

### Configurar Firewall (se necessário)

#### Windows:
1. Abra o "Firewall do Windows Defender"
2. Clique em "Configurações avançadas"
3. Clique em "Regras de entrada" → "Nova regra"
4. Selecione "Porta" → "TCP" → "Portas específicas" → "8000"
5. Permita a conexão

#### Linux (Ubuntu/Debian):
```bash
sudo ufw allow 8000
```

## 🧪 Testando a Conectividade

### 1. Teste Local
Acesse `http://localhost:8000/status` no navegador.
Deve retornar: `{"status": "online", "message": "Servidor funcionando corretamente"}`

### 2. Teste de Rede
Em outro computador, acesse `http://[IP_DA_MAQUINA]:8000/status`
Deve retornar a mesma mensagem de status.

## 🔄 Funcionalidades

- ✅ **Dados Compartilhados**: Todos os computadores acessam os mesmos dados
- ✅ **Tempo Real**: Alterações são refletidas imediatamente
- ✅ **Múltiplos Usuários**: Cada usuário tem seus próprios dados
- ✅ **Backup Automático**: Dados são salvos no servidor

## 🛠️ Solução de Problemas

### Erro de Conexão
1. Verifique se o servidor está rodando
2. Confirme o IP da máquina
3. Teste a conectividade: `ping [IP_DA_MAQUINA]`
4. Verifique o firewall

### Dados Não Aparecem
1. Verifique se está usando o mesmo usuário
2. Recarregue a página
3. Verifique o console do navegador (F12)

### Servidor Não Inicia
1. Verifique se a porta 8000 está livre
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute como administrador (se necessário)

## 📱 Acesso Mobile

O sistema também funciona em dispositivos móveis na mesma rede:
- Acesse `http://[IP_DA_MAQUINA]:8000` no navegador do celular
- Interface responsiva para mobile

## 🔒 Segurança

⚠️ **Importante**: Este servidor é para uso em rede local apenas.
- Não exponha na internet
- Use apenas em redes confiáveis
- Para produção, implemente autenticação e HTTPS

## 📞 Suporte

Se encontrar problemas:
1. Verifique os logs do servidor
2. Teste a conectividade de rede
3. Reinicie o servidor se necessário