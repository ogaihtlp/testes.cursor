#!/usr/bin/env python3
"""
Servidor simples para o Sistema de Gestão Pessoal
Permite acesso em rede local para testes
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios

# Dados em memória (em produção, usar banco de dados)
data = {
    'monthly': [],
    'travel': []
}

# Contador de IDs
next_id = 1

def get_next_id():
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

@app.route('/')
def index():
    """Serve o arquivo HTML principal"""
    return send_from_directory('.', 'controle de dados.html')

@app.route('/monthly/', methods=['GET', 'POST'])
def monthly_data():
    """Gerencia dados mensais"""
    if request.method == 'GET':
        user = request.args.get('user', '')
        periodo = request.args.get('periodo', '')
        tipo = request.args.get('tipo', '')
        
        # Filtrar dados
        filtered_data = []
        for item in data['monthly']:
            if user and item.get('user') != user:
                continue
            if periodo and not item.get('periodo_mes', '').startswith(periodo):
                continue
            if tipo and item.get('tipo_atendimento') != tipo:
                continue
            filtered_data.append(item)
        
        return jsonify(filtered_data)
    
    elif request.method == 'POST':
        new_data = request.get_json()
        new_data['id'] = get_next_id()
        new_data['created_at'] = datetime.now().isoformat()
        data['monthly'].append(new_data)
        return jsonify(new_data), 201

@app.route('/monthly/<int:item_id>', methods=['PUT', 'DELETE'])
def monthly_item(item_id):
    """Gerencia um item específico de dados mensais"""
    user = request.args.get('user', '')
    
    # Encontrar o item
    item = None
    for i, data_item in enumerate(data['monthly']):
        if data_item['id'] == item_id and data_item.get('user') == user:
            item = data_item
            item_index = i
            break
    
    if not item:
        return jsonify({'error': 'Item não encontrado'}), 404
    
    if request.method == 'PUT':
        update_data = request.get_json()
        update_data['id'] = item_id
        update_data['user'] = user
        update_data['updated_at'] = datetime.now().isoformat()
        data['monthly'][item_index] = update_data
        return jsonify(update_data)
    
    elif request.method == 'DELETE':
        del data['monthly'][item_index]
        return jsonify({'message': 'Item excluído com sucesso'})

@app.route('/travel/', methods=['GET', 'POST'])
def travel_data():
    """Gerencia dados de viagem"""
    if request.method == 'GET':
        user = request.args.get('user', '')
        data_inicio = request.args.get('data_inicio', '')
        data_fim = request.args.get('data_fim', '')
        cidade = request.args.get('cidade', '')
        
        # Filtrar dados
        filtered_data = []
        for item in data['travel']:
            if user and item.get('user') != user:
                continue
            if data_inicio and item.get('data_inicio', '') < data_inicio:
                continue
            if data_fim and item.get('data_fim', '') > data_fim:
                continue
            if cidade and cidade.lower() not in item.get('cidade', '').lower():
                continue
            filtered_data.append(item)
        
        return jsonify(filtered_data)
    
    elif request.method == 'POST':
        new_data = request.get_json()
        new_data['id'] = get_next_id()
        new_data['created_at'] = datetime.now().isoformat()
        data['travel'].append(new_data)
        return jsonify(new_data), 201

@app.route('/travel/<int:item_id>', methods=['PUT', 'DELETE'])
def travel_item(item_id):
    """Gerencia um item específico de dados de viagem"""
    user = request.args.get('user', '')
    
    # Encontrar o item
    item = None
    for i, data_item in enumerate(data['travel']):
        if data_item['id'] == item_id and data_item.get('user') == user:
            item = data_item
            item_index = i
            break
    
    if not item:
        return jsonify({'error': 'Item não encontrado'}), 404
    
    if request.method == 'PUT':
        update_data = request.get_json()
        update_data['id'] = item_id
        update_data['user'] = user
        update_data['updated_at'] = datetime.now().isoformat()
        data['travel'][item_index] = update_data
        return jsonify(update_data)
    
    elif request.method == 'DELETE':
        del data['travel'][item_index]
        return jsonify({'message': 'Item excluído com sucesso'})

@app.route('/status')
def status():
    """Endpoint de status para verificar se o servidor está funcionando"""
    return jsonify({
        'status': 'online',
        'message': 'Servidor funcionando corretamente',
        'total_monthly': len(data['monthly']),
        'total_travel': len(data['travel'])
    })

if __name__ == '__main__':
    print("🚀 Iniciando servidor do Sistema de Gestão Pessoal...")
    print("📊 Acesse: http://localhost:8000")
    print("🌐 Para rede local, use o IP da sua máquina")
    print("💡 Exemplo: http://192.168.1.100:8000")
    print("🔄 Pressione Ctrl+C para parar o servidor")
    
    # Executar o servidor
    app.run(host='0.0.0.0', port=8000, debug=True)